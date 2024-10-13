import jwt
from datetime import datetime, timedelta
from django.conf import settings
from higher_control.user_control.models import CustomUser
from rest_framework.pagination import PageNumberPagination
import re
from django.db.models import Q


def create_access_token(id, minutes):
    token = jwt.encode(
        {
            "user_id": id,
            "exp": datetime.utcnow() + timedelta(minutes=minutes), 
            "iat": datetime.utcnow(),         },
        settings.SECRET_KEY,
        algorithm="HS256"
    )
    return token

def create_refresh_token(id, days):
    refresh = jwt.encode(
        {
            "user_id": id,
            "exp": datetime.utcnow() + timedelta(days=days), 
            "iat": datetime.utcnow(), 
        },
        settings.SECRET_KEY,
        algorithm="HS256"
    )
    return refresh


def extract_access_token(bearer):
    if not bearer:
        return None
    token = bearer[7:]
    try:
        decoded = jwt.decode(
            token, key=settings.SECRET_KEY, algorithms="HS256"
        )
    except:
        return None

    if decoded:
        try:
            return CustomUser.objects.get(id=decoded["user_id"])
        except:
            return None
        

def verify_token(bearer):
    if not bearer:
        return None
    token = bearer[7:]

    try:
        decoded = jwt.verify(
            token, key=settings.SECRET_KEY, algorithms="HS256"
        )
    except:
        return None

    if decoded:
        try:
            return CustomUser.objects.get(id=decoded["user_id"])
        except:
            return None


class CustomPagination(PageNumberPagination):
    page_size = 50
    max_page_size = 50
    page_size_query_param = "size"
    page_query_param = "page"


class ResultPagination(PageNumberPagination):
    page_size = 10000
    max_page_size = 10000
    page_size_query_param = "size"
    page_query_param = "page"

def normalize_query(
        query_string,
        findterms=re.compile(r'"([^"]+)"|(\S+)').findall, normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    def convertBooleanNone(item):
        if (item == "true"):
            return 1
        elif (item == "false"):
            return 0
        elif (item == "None"):
            return None
        else:
            return item
    query = None

    try:
        terms = normalize_query(query_string)
        for t in terms:
            term = convertBooleanNone(t)
            or_query = None     # Query to search for a given term in each field
            for field_name in search_fields:
                q = Q(**{"%s__icontains" % field_name: term})
                if or_query is None:
                    or_query = q
                else:
                    or_query = or_query | q
            if query is None:
                query = or_query
            else:
                query = query & or_query
            return query
    except:
        i = 0
        for t in query_string:
            term = convertBooleanNone(t)
            or_query = None     # Query to search for a given term in each field
            q = Q(**{"%s__icontains" % search_fields[i]: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
            if query is None:
                query = or_query
            else:
                query = query & or_query
            i += 1
        return query

    
def get_query_exact(query_string, search_fields):
    def convertBooleanNone(item):
        if (item == "true"):
            return 1
        elif (item == "false"):
            return 0
        elif (item == "None"):
            return None
        else:
            return item
    query = None

    try:
        terms = normalize_query(query_string)
        for t in terms:
            term = convertBooleanNone(t)
            or_query = None     # Query to search for a given term in each field
            for field_name in search_fields:
                q = Q(**{"%s__exact" % field_name: term})
                if or_query is None:
                    or_query = q
                else:
                    or_query = or_query | q
            if query is None:
                query = or_query
            else:
                query = query & or_query
            return query
    except:
        i = 0
        for t in query_string:
            term = convertBooleanNone(t)
            or_query = None     # Query to search for a given term in each field
            q = Q(**{"%__exact" % search_fields[i]: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
            if query is None:
                query = or_query
            else:
                query = query & or_query
            i += 1
        return query

    
def querydict_to_dict(query_dict):
    data = {}
    for key in query_dict.keys():
        v = query_dict.getlist(key)
        if len(v) == 1:
            v = v[0]
        data[key] = v
    return data
