from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class SignUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = "User"
        fields = ["first_name", "last_name", "email", "password"]
        extra_kwargs = {
            "first_name": {
                "required": True,
                "allow_blank": False
            },
            "last_name": {
                "required": True,
                "allow_blank": False
            },
            "email": {
                "required": True,
                "allow_blank": False,
                "min_length": 1
            },
            "password": {
                "required": True,
                "allow_blank": False,
                 "min_length": 5
            },
        }

class UserSerializer(serializers.ModelSerializer):
    resume = serializers.CharField(source="userprofile.resume")
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "email", "password", "resume"]