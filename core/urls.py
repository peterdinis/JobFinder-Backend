from django.contrib import admin
from django.urls import path, include
from rest_framework_yasg.views import get_schema_view
from rest_framework_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="JobFinder API",
        default_version='v1',
        description="API documentation for the JobFinder project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@jobfinder.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("jobs.urls")),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
]