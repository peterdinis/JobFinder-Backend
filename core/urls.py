from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("jobs/", include("jobs.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/token/", TokenObtainPairView.as_view()),
    path("accounts/token/verify", TokenVerifyView.as_view()),
    
]

handler500 = "utils.error_views.handler500"
handler404 = "utils.error_views.handler404"
