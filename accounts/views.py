from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializers import SignUpSerializers, UserSerializer
from django.contrib.auth.models import User

@api_view(["POST"])
def register_user(request):
    data = request.data

    # Initialize the serializer with the provided data
    user_serializer = SignUpSerializers(data=data)

    if user_serializer.is_valid():
        # Check if a user with the provided email already exists
        if User.objects.filter(username=data["email"]).exists():
            return Response({"message": "User with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user if email is not taken
        user_data = user_serializer.validated_data
        user = User(
            username=user_data["email"],  # use email as username
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
            password=make_password(user_data["password"]),  # Hash the password
        )
        user.save()

        # Serialize the created user and return a response
        response_serializer = UserSerializer(user)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)