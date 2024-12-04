from django_tenants.middleware.main import TenantMainMiddleware
from django.conf import settings
from django.http import JsonResponse
from rest_framework import permissions


class TenantMiddleware(TenantMainMiddleware):
    """
    Field is_active can be used to temporary disable tenant """
    def get_tenant(self, domain_model, hostname):
        tenant = super().get_tenant(domain_model, hostname)
        if not tenant.is_active:
            raise self.TENANT_NOT_FOUND_EXCEPTION("Tenant is Inactive")
        return tenant


class APIKeyMiddleware:             # ADD THIS TO MIDDLEWARE IN settings.py
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get("X-API-Key")
        if api_key != settings.API_KEY:
            return JsonResponse({"error": "Unauthorized"}, status=401)
        return self.get_response(request)
    

class IsAuthenticatedWithAPIKey(permissions.BasePermission):
    def has_permission(self, request, view):
        if settings.USE_API_KEY:
            api_key = request.headers.get('X-API-Key')
            print(api_key, 3222222222222222222222222222222222)
            return api_key == settings.API_KEY
        else:
            return True
    
    