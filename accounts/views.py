from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from reset_framework import status
from django.contrib.auth.hashers import make_password
from .serializers import SignUpSerializers, UserSerializer
from django.contrib.auth.models import User

@api_view(["POST"])
def register_user(request):
    pass