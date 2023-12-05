from rest_framework.permissions import BasePermission
from rest_framework.views import exception_handler
from rest_framework.response import Response
from .utils import extract_access_token


class IsAuthenticatedCustom(BasePermission):

    def has_permission(self, request, view):
        print(request.META.get("HTTP_AUTHORIZATION", None))
        try:
            auth_token = request.META.get("HTTP_AUTHORIZATION", None).split()[1]
        except:
            return False
        if not auth_token:
            return False
        # print("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MDE2NzEwMjksImlhdCI6MTcwMTY3MDQyOX0.GPeQsnjSp71TCsMCO6lXhYuHhqmtdNCffW-xhROVC64")
        user = extract_access_token(auth_token)
        print(user)

        if not user:
            return False

        request.user = user
        return True


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return response
    
    exc_list = str(exc).split("DETAIL: ")

    return Response({ "error": exc_list[-1] }, status=403)