from django_tenants.middleware.main import TenantMainMiddleware
from django.conf import settings
from django.http import JsonResponse
from rest_framework import permissions
import json
from urllib.parse import urlparse, parse_qs
from django.middleware.cache import CacheMiddleware



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
    

class RestrictGraphQLMiddleware:             # ADD THIS TO MIDDLEWARE IN settings.py
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only apply to GraphQL endpoint
        if request.path == "/graphql/":
            # Block if the request contains URL query parameters or fragments
            parsed_url = urlparse(request.get_full_path())
            query_params = parse_qs(parsed_url.query)
            fragment = parsed_url.fragment

            if query_params or fragment:
                return JsonResponse(
                    {"error": "Direct URL-based queries are not allowed."},
                    status=400
                )

            # For POST requests, check the request body
            if request.method == "POST":
                try:
                    # Load JSON body
                    body = json.loads(request.body)

                    # Extract query and variables
                    query = body.get("query", None).strip()
                    variables = body.get("variables", None)

                    # Check if the query is empty or null
                    if not query:
                        return JsonResponse(
                            {"error": "GraphQL query cannot be empty or null."},
                            status=400
                        )

                    # Check if variables are present but invalid (null or empty dict)
                    if variables is not None and not isinstance(variables, dict):
                        return JsonResponse(
                            {"error": "Invalid variables format. Should be a JSON object."},
                            status=400
                        )

                except json.JSONDecodeError:
                    # Handle invalid JSON payload
                    return JsonResponse(
                        {"error": "Invalid JSON payload."},
                        status=400
                    )

        return self.get_response(request)
    

class IsAuthenticatedWithAPIKey(permissions.BasePermission):
    def has_permission(self, request, view):
        if settings.USE_API_KEY:
            api_key = request.headers.get('X-API-Key')
            return api_key == settings.API_KEY
        else:
            return True
    
# class DisableGraphQLCacheMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         if request.path == "/graphql/":
#             patch_cache_control(response, no_cache=True, no_store=True, must_revalidate=True)
#         return response


class CustomCacheMiddleware(CacheMiddleware):
    def process_response(self, request, response):
        if '/graphql/' in request.path:  # Replace with your GraphQL endpoint path
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        return response
