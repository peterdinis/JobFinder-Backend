from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import SignUpSerializers, UserProfileSerializer
from django.contrib.auth.models import User
from .models import UserProfile

@api_view(["POST"])
def register_user(request):
    """
    Register a new user.
    """
    data = request.data
    user_serializer = SignUpSerializers(data=data)

    if user_serializer.is_valid():
        if User.objects.filter(username=data["email"]).exists():
            return Response({"message": "User with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user_data = user_serializer.validated_data
        user = User(
            username=user_data["email"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
            password=make_password(user_data["password"]),
        )
        user.save()

        response_serializer = UserProfileSerializer(user)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def currentUser(request):
    """
    Retrieve the current authenticated user's information.
    """
    user = request.user
    serializer = UserProfileSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_all_users(request):
    """
    Retrieve a list of all users (admin only).
    """
    users = User.objects.all()
    serializer = UserProfileSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request, pk):
    """
    Retrieve a specific user by ID.
    """
    user = get_object_or_404(User, pk=pk)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user(request, pk):
    """
    Update a user's information.
    """
    user = get_object_or_404(User, pk=pk)
    if user != request.user and not request.user.is_staff:
        return Response({"message": "You are not authorized to update this user."}, status=status.HTTP_403_FORBIDDEN)

    serializer = UserProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_user(request, pk):
    """
    Delete a user (admin only).
    """
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_user_profile(request):
    """
    Create a user profile for the authenticated user.
    """
    data = request.data
    data["user"] = request.user.id  # Associate the profile with the authenticated user
    serializer = UserProfileSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    """
    Retrieve the authenticated user's profile.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    serializer = UserProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    """
    Update the authenticated user's profile.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    serializer = UserProfileSerializer(profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def upload_resume(request):
    """
    Upload a resume for the authenticated user.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # Check if a file is provided
    if 'resume' not in request.FILES:
        return Response({"message": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)

    resume = request.FILES['resume']

    # Optional: Validate file type (only PDF, DOCX, etc.)
    if not resume.name.endswith(('.pdf', '.docx', '.txt')):
        return Response({"message": "Invalid file type. Only PDF, DOCX, and TXT are allowed."}, status=status.HTTP_400_BAD_REQUEST)

    # Optional: Validate file size (limit to 5MB)
    if resume.size > 5 * 1024 * 1024:  # 5MB
        return Response({"message": "File is too large. Maximum size is 5MB."}, status=status.HTTP_400_BAD_REQUEST)

    # Update the user's profile with the new resume
    profile.resume = resume
    profile.save()

    # Return response with updated user profile data
    serializer = UserProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)