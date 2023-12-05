import jwt
from datetime import datetime, timedelta
from django.conf import settings
from user_control.models import CustomUser
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
    page_size = 500


def normalize_query(
        query_string,
        findterms=re.compile(r'"([^"]+)"|(\S+)').findall, normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    query = None
    terms = normalize_query(query_string)
    for term in terms:
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
