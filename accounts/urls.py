from django.urls import path
from . import views

urlpatterns = [
    # User management endpoints
    path("register/", views.register_user, name="register_user"),
    path("current-user/", views.currentUser, name="current_user"),
    path("users/", views.get_all_users, name="get_all_users"),
    path("users/<int:pk>/", views.get_user, name="get_user"),
    path("users/<int:pk>/update/", views.update_user, name="update_user"),
    path("users/<int:pk>/delete/", views.delete_user, name="delete_user"),

    # User profile endpoints
    path("user-profile/", views.get_user_profile, name="get_user_profile"),
    path('upload_resume/', views.upload_resume, name='upload_resume'),
    path("user-profile/create/", views.create_user_profile, name="create_user_profile"),
    path("user-profile/update/", views.update_user_profile, name="update_user_profile"),
]