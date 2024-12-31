from django.urls import path
from . import views

urlpatterns = [
    path("jobs/", views.get_all_jobs, name="get_all_jobs"),
    path("jobs/create/", views.create_job, name="create_job"),
    path("jobs/<int:pk>/", views.get_job, name="get_job"),
    path("jobs/<int:pk>/update/", views.update_job, name="update_job"),
    path("jobs/<int:pk>/delete/", views.delete_job, name="delete_job"),
]