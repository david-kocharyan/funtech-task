from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.inspectors import SwaggerAutoSchema
from rest_framework.pagination import PageNumberPagination


class CustomCursorPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    page_query_param = 'page'
    ordering = "-id"


class CustomSwaggerAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        operation_keys = operation_keys or self.operation_keys
        tags = self.overrides.get('tags')
        tags and print(tags)
        if not tags:
            tags = [operation_keys[0]]
        if hasattr(self.view, "swagger_tags"):
            tags = self.view.swagger_tags

        return tags


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema
