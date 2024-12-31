from django.urls import path
from . import views

urlpatterns = [
    path("jobs/", views.get_all_jobs, name="jobs")
]