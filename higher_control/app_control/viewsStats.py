from rest_framework.viewsets import ViewSet
from django.core import serializers
from rest_framework.permissions import IsAuthenticated
from django.db.models.functions import Coalesce
from back.utils import *
from django.db.models import Q, Sum
from rest_framework.response import Response
from .serializers import *
from .dataUpdates import *
from higher_control.fees_control.serializers import SchoolFees, Transactions, SchoolFeesSerializer
from .filters import *
from django_filters import rest_framework as filters
import datetime

# list_of_months = [datetime.date(2024, i, 1).strftime('%B') for i in range(1, 13)]
list_of_months_short = [ [ str(i).zfill(2), datetime.date(2024, i, 1).strftime('%B')[:3], datetime.date(2024, i, 1).strftime('%B') ] for i in range(1, 13)]
list_of_months_acad_one = list_of_months_short[-4:]
list_of_months_acad_two = list_of_months_short[:8]

def qInc(reasons):
    incVals = ['REGISTRATION', 'TUITION']
    initVal = Q( reason__icontains=incVals[0] )
    if reasons and len(reasons):
        for val in reasons:
            initVal = Q( reason__icontains=val )
    else:
        for val in incVals[1:]:
            initVal = initVal | Q( reason__icontains=val )
    return initVal


def customQuery(params):
    keysList = list(params.keys())
    for k in keysList:
        if not params[k]:
            params.pop(k)
    return params


def studStats(studList, sf, y):
    count = studList.count()
    total = 0
    balance = 0
    for s in sf:
        total += s.userprofile.specialty.tuition
        balance += s.balance
    return { "count": count, "total": total, "paid": total - balance, "balance": balance, "year": y }


def sumAmountTransactions(trans):
    total = 0
    for t in trans:
        total += t.amount
    return total


class GetStatsByDomainView(ViewSet):
    http_method_names = [ "get" ]

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        p = {
            "userprofile__specialty__school__id": param.pop("school", None),
            "userprofile__specialty__academic_year": param.pop("academic_year", None),
            "userprofile__specialty__main_specialty__field__domain__id": param.pop("domain", None),
        }
        studQuery = {
            "user__role": "student", 
            "specialty__academic_year": p["userprofile__specialty__academic_year"], 
            "specialty__school__id": p["userprofile__specialty__school__id"], 
        }
        if p["userprofile__specialty__main_specialty__field__domain__id"]:
            allDomains = Domain.objects.filter(id=p["userprofile__specialty__main_specialty__field__domain__id"]).order_by("domain_name")
        else:
            allDomains = Domain.objects.all().order_by("domain_name")
        res = []

        if p["userprofile__specialty__academic_year"] and allDomains and p["userprofile__specialty__main_specialty__field__domain__id"]:
            d = Domain.objects.get(id=p["userprofile__specialty__main_specialty__field__domain__id"])
            dStud = UserProfile.objects.filter(**studQuery, specialty__main_specialty__field__domain__id=1)
            dSF = SchoolFees.objects.filter(**customQuery(p))
            res.append({ **studStats(dStud, dSF, p["userprofile__specialty__academic_year"]), "domain_name": d.domain_name })      
        if p["userprofile__specialty__academic_year"] and allDomains and not p["userprofile__specialty__main_specialty__field__domain__id"]:
            for d in allDomains:
                dStud = UserProfile.objects.filter(**customQuery(studQuery), specialty__main_specialty__field__domain__id=d.id)
                dSF = SchoolFees.objects.filter(**customQuery(p), userprofile__specialty__main_specialty__field__domain__id=d.id)
                res.append({ **studStats(dStud, dSF, p["userprofile__specialty__academic_year"]), "domain_name": d.domain_name })      
        res = [item for item in res if item["count"] > 0]
        return Response(res)
    

class GetStatsBySpecialtyView(ViewSet):
    http_method_names = [ "get" ]

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        a = {
            "school__id": param.pop("school", None),
            "academic_year": param.pop("academic_year", None),
            "main_specialty__field__domain__id": param.pop("domain", None),
            "level__id": param.pop("level", None),
        }
        b = {
            "user__role": "student",
            "specialty__academic_year": a["academic_year"],
            "specialty__id": param.pop("specialty", None),
        }
        spec = Specialty.objects.filter(**customQuery(a)).order_by("main_specialty__specialty_name")
        res = []
        
        if spec and a["academic_year"] and b["specialty__id"]:
            s = spec.get(id=b["specialty__id"])
            sStud = UserProfile.objects.filter(**customQuery(b))
            sSF = SchoolFees.objects.filter(userprofile__specialty__academic_year=a["academic_year"], userprofile__specialty__id=s.id)
            res.append({ **studStats(sStud, sSF, a["academic_year"]), "specialty_name": s.main_specialty.specialty_name })   
        if spec and a["academic_year"] and not b["specialty__id"]:
            for s in spec:
                sStud = UserProfile.objects.filter(**customQuery(b), specialty__id=s.id)
                sSF = SchoolFees.objects.filter(userprofile__specialty__academic_year=a["academic_year"], userprofile__specialty__id=s.id)
                res.append({ **studStats(sStud, sSF, a["academic_year"]), "specialty_name": s.main_specialty.specialty_name, "level": s.level.level })      
        return Response([item for item in res if item["count"] > 0])
    

class GetStatsStudentsPendingFeesView(ViewSet):
    #example => get-stats-students-pending-fees?academic_year=2022/2023&bal=270001&type_id=c1&fieldList=id,balance,userprofile__user__full_name,balance,userprofile__user__id
    http_method_names = [ "get" ]
    serializer_class = SchoolFeesSerializer

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        searchSchool = param.pop("school", None)
        acadYear = param.pop("academic_year", None)
        searchTypeAndID = param.pop("type_id", None)        #example s4 => s=specialty ID=4, c4 => c=campus, ID=2
        balance = param.pop("bal", 0)                    #example bal => balance
        fieldList = param.pop("fieldList", None)                   #example bal => balance
        res = []

        if fieldList and acadYear and balance and searchSchool:
            res = SchoolFees.objects.filter(userprofile__specialty__school__id=searchSchool, balance__gte=balance, userprofile__specialty__academic_year=acadYear)
            if searchTypeAndID:
                if searchTypeAndID[0] == "d":
                    res = res.filter( userprofile__specialty__main_specialty__field__domain__id=searchTypeAndID[1:])
                if searchTypeAndID[0] == "s":
                    res = SchoolFees.objects.filter(userprofile__specialty__id=searchTypeAndID[1:])
            return Response([r for r in res.values(*fieldList.split(",")) ])
        return Response([])
    

class GetStatsUserCardCountView(ViewSet):
    http_method_names = [ "get" ]

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        searchSchool = param.pop("school", None)
        statsYear = param.pop("academic_year", None)
        admins = CustomUser.objects.filter(role="admin", is_active=True, is_staff=False, school__id=searchSchool)
        lecturers = CustomUser.objects.filter(role="teacher", is_active=True, is_staff=False, school__id=searchSchool)
        students = UserProfile.objects.filter(specialty__school__id=searchSchool, specialty__academic_year=statsYear, user__role="student", user__is_active=True, user__is_staff=False)
        inactive = UserProfile.objects.filter(user__is_active=False, user__is_staff=False)
        res = []

        if statsYear:
            return Response({ "students": students.count(), "lecturers": lecturers.count(), "admins": admins.count(), "inactive": inactive.count(), "academic_year": statsYear })      
        return Response(res)
    

class GetStatsFinanceChartView(ViewSet):
    http_method_names = [ "get" ]

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        searchSchool= param.pop("school", None)
        thisYear = param.pop("this_year", None)
        acadYear = param.pop("academic_year", None)
        period = param.pop("period", None)
        reasons = param.pop("reasons", None)
        a = {
            "schoolfees__userprofile__specialty__school__id": searchSchool,
            "created_at__year__gte": acadYear[0:4],
            "created_at__year__lte": acadYear[5:9],
        }
        transaction_between_period = Transactions.objects.filter(**customQuery(a)).filter(qInc(reasons))
        print(transaction_between_period)
        res = []
        if period and period == "ac_year":
            for month in list_of_months_acad_one:
                month_filter = transaction_between_period.filter(created_at__year=acadYear[0:4], created_at__month=month[0])
                month_filter_registration = month_filter.filter(reason="REGISTRATION")
                month_filter_tuition = month_filter.filter(reason="TUITION")
                month_filter_scholarship = month_filter.filter(reason="SCHOLARSHIP")
                res.append({ 
                    "month": month[1],
                    "registration": month_filter_registration.aggregate(total_amount=Coalesce(Sum('amount'), 0))["total_amount"],
                    "tuition": month_filter_tuition.aggregate(total_amount=Coalesce(Sum('amount'), 0))["total_amount"],
                    "scholarship": month_filter_scholarship.aggregate(total_amount=Coalesce(Sum('amount'), 0))["total_amount"],
                })
            for month in list_of_months_acad_two:
                month_filter = transaction_between_period.filter(created_at__year=acadYear[5:9], created_at__month=month[0])
                res.append({ 
                    "month": month[1],
                    "registration": month_filter.filter(reason="REGISTRATION").aggregate(total_amount=Coalesce(Sum('amount'), 0))["total_amount"],
                    "tuition": month_filter.filter(reason="TUITION").aggregate(total_amount=Coalesce(Sum('amount'), 0))["total_amount"],
                    "scholarship": month_filter.filter(reason="SCHOLARSHIP").aggregate(total_amount=Coalesce(Sum('amount'), 0))["total_amount"],
                })
        else:
            for month in list_of_months_short:
                month_filter = transaction_between_period.filter(created_at__year=thisYear, created_at__month=month[0])
                res.append({ 
                    "month": month[1],
                    "registration": month_filter.filter(reason="REGISTRATION").aggregate(total_amount=Coalesce(Sum('amount'), 0))["total_amount"],
                    "tuition": month_filter.filter(reason="TUITION").aggregate(total_amount=Coalesce(Sum('amount'), 0))["total_amount"],
                    "scholarship": month_filter.filter(reason="SCHOLARSHIP").aggregate(total_amount=Coalesce(Sum('amount'), 0))["total_amount"],
                })
        return Response(res)


class GetStatsBySpecialtyAndLevelIncomeView(ViewSet):
    http_method_names = [ "get" ]

    def list(self, request):

        param = querydict_to_dict(self.request.query_params)
        acadYear = param.pop("academic_year", None)
        searchSchool= param.pop("school", None)
        reasons = param.pop("reasons", None)
        period = param.pop("period", None)
        a = {
            "schoolfees__userprofile__specialty__school__id": searchSchool,
            "created_at__year__gte": acadYear[0:4],
            "created_at__year__lte": acadYear[5:9],
        }
        b = {
            "schoolfees__userprofile__specialty__school__id": searchSchool,
            "schoolfees__userprofile__specialty__academic_year": acadYear,
        }
        if period == "ac_year":
            transations = Transactions.objects.filter(**customQuery(b)).filter(qInc(reasons))
        else:
            transations = Transactions.objects.filter(**customQuery(a)).filter(qInc(reasons))
        mainspecialties = MainSpecialty.objects.all().order_by("specialty_name")
        specialties = Specialty.objects.filter(school__id=searchSchool, academic_year=acadYear).order_by("main_specialty__specialty_name")
        levels = Level.objects.all().order_by("level")
        res = []

        if acadYear and mainspecialties and specialties and levels:
            for ms in mainspecialties:
                item = { "specialty_name": ms.specialty_name_short }
                filSpec = specialties.filter(main_specialty__specialty_name=ms.specialty_name)
                if filSpec:
                    specTrans = transations.filter(schoolfees__userprofile__specialty__main_specialty__specialty_name=filSpec.first().main_specialty.specialty_name)
                    if specTrans:
                        item["academic_year"] = acadYear
                        for l in levels:
                            levFees = specTrans.filter(schoolfees__userprofile__specialty__level__level=l.level)
                            item["level_" + str(l.level)] = sumAmountTransactions(levFees)
                        res.append(item) 
        return Response(res)
    

class GetStatsBySpecialtiesAndLevelsView(ViewSet):
    http_method_names = [ "get" ]

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        searchSchool = param.pop("school", None)
        acadYear = param.pop("academic_year", None)
        acadStud = UserProfile.objects.filter(specialty__academic_year=acadYear, specialty__school__id=searchSchool)
        mainspecialties = MainSpecialty.objects.all().order_by("specialty_name")
        specialties = Specialty.objects.filter(academic_year=acadYear, school__id=searchSchool).order_by("main_specialty__specialty_name")
        levels = Level.objects.all().order_by("level")
        res = []

        if acadYear and mainspecialties and specialties and levels:
            for ms in mainspecialties:
                item = { "specialty_name": ms.specialty_name_short }
                item["academic_year"] = acadYear
                filSpec = specialties.filter(main_specialty__specialty_name=ms.specialty_name)
                if filSpec:
                    specStud = acadStud.filter(specialty__main_specialty__specialty_name=filSpec.first().main_specialty.specialty_name)
                    if specStud:
                        for l in levels:
                            levStud = specStud.filter(specialty__level__level=l.level)
                            item[l.level] = levStud.count()
                        res.append(item)   
        return Response(res)


class GetStatsSexChartView(ViewSet):
    http_method_names = [ "get" ]

    def list(self, request):
        param = querydict_to_dict(self.request.query_params)
        searchSchool= param.pop("school", None)
        statsYear = param.pop("academic_year", None)
        profs = UserProfile.objects.filter(specialty__academic_year=statsYear, specialty__school__id=searchSchool)
        maleProfs = profs.filter(user__sex="Male").count()
        femaleProfs = profs.filter(user__sex="Female").count()
        res = []
        if profs:
            res = [
                # { "name": "Total", "count": profs.count(), "percent": 100 },
                { "name": "Male", "count": maleProfs, "percent": round( (maleProfs/profs.count()) * 100) },
                { "name": "Female", "count": femaleProfs, "percent": round( (femaleProfs/profs.count()) * 100) },
            ]
        
        return Response(res)

