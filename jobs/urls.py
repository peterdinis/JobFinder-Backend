from django.urls import path
from . import views

urlpatterns = [
    path("jobs/", views.get_all_jobs, name="get_all_jobs"),
    path("jobs/create/", views.create_job, name="create_job"),
    path("jobs/<int:pk>/", views.get_job, name="get_job"),
    path("jobs/<int:pk>/update/", views.update_job, name="update_job"),
    path("jobs/<int:pk>/delete/", views.delete_job, name="delete_job"),
    path("stats/<str:topic>/", views.get_topic_stats, name="topic_stats"),
    path("jobs/<int:pk>/apply/", views.apply_to_job, name="apply_to_job"),
    path('user/application_count/', views.get_user_application_count, name='get_user_application_count'),
    path('jobs/<int:pk>/is_applied/', views.is_applied, name='is_applied'),
    path('user/current_jobs/', views.get_current_user_jobs, name='get_current_user_jobs'),
]