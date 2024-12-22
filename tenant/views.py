from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from back.utils import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
# from django.contrib.auth.mixins import PermissionRequiredMixin
from .filters import *
from django_filters import rest_framework as filters

class BaseModelViewSet(ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        return self.queryset.order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class BaseGetViewSet(ModelViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    
    def get_queryset(self):
        param = querydict_to_dict(self.request.query_params)
        field_list = param.pop("fieldList", None)
        queryset = super().get_queryset()

        if field_list:
            field_list = field_list.split(',')

            # Get serializer fields
            serializer_fields = self.get_serializer().fields

            # Separate relational and non-relational fields
            relational_fields = []
            non_relational_fields = []
            other_fields = []
            for field_name in field_list:

                if field_name in serializer_fields:
                    field = serializer_fields[field_name]
                    if hasattr(field, "source") and "." in field.source and field.source.count(".") == 1:
                        orm_field = field.source.replace(".", "__")
                        relational_fields.append(orm_field)
                    if hasattr(field, "source") and "." in field.source and field.source.count(".") == 1:
                        orm_field = field.source.replace(".", "__")
                        other_fields.append(orm_field)
                    else:
                        non_relational_fields.append(field_name)

            # Apply select_related for relational fields
            if relational_fields:
                queryset = queryset.select_related(*relational_fields)

            non_relational_fields = [
                field for field in non_relational_fields if field not in relational_fields
            ]
            if non_relational_fields:
                queryset = queryset.only(*set(non_relational_fields))

        return queryset
    

    def paginate_queryset(self, queryset):
        param = querydict_to_dict(self.request.query_params)
        nopage = param.pop("nopage", None)
        if nopage:
            return None
        return super().paginate_queryset(queryset)

    def perform_query_optimization(self, queryset, related_fields=None):
 
        if related_fields:
            queryset = queryset.select_related(*related_fields)
        return queryset
    
    def get_serializer(self, *args, **kwargs):
        """
        Dynamically filter serializer fields based on `fieldList`.
        """
        field_list = self.request.query_params.get("fieldList")
        if field_list:
            fields = field_list.split(',')
            kwargs["fields"] = fields
        return super().get_serializer(*args, **kwargs)
    

class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Extract 'fields' from kwargs to limit returned fields
        fields = kwargs.pop("fields", None)
        super().__init__(*args, **kwargs)
        if fields:
            # Remove any fields not in the provided `fields` list
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class TenantView(BaseModelViewSet):
    http_method_names = [ "get", "post", "put", "delete"]
    queryset = Tenant.objects.all().order_by("id")
    serializer_class = TenantSerializer
    filterset_class = TenantFilter
    # permission_classes = [ IsAuthenticated ]


class DomView(BaseModelViewSet):
    http_method_names = [ "get", "post", "put", "delete"]
    queryset = Domain.objects.all().order_by("id")
    serializer_class = DomSerializer
    filterset_class = DomFilter
    # permission_classes = [ IsAuthenticated ]

