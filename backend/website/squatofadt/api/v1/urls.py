from django.urls import path, include
from rest_framework.schemas import get_schema_view

from squatofadt.api.openapi import OpenAPISchemaGenerator

app_name = "squatofadt"

urlpatterns = [
    path("exercises/", include("exercises.api.v1.urls")),
    path(
        "schema",
        get_schema_view(
            title="API v1",
            url="/api/v1/",
            version=1,
            urlconf="squatofadt.api.v1.urls",
            generator_class=OpenAPISchemaGenerator,
        ),
        name="schema-v1",
    ),
]
