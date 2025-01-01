from rest_framework import serializers
from .models import *

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class CandidatesAppieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidatesAppield
        fields = "__all__"