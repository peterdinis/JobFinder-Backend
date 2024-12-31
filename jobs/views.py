from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobSerializer
from .models import Job

@api_view(["GET"])
def get_all_jobs(request):
    """
    Retrieve all jobs from the database and return them as a serialized JSON response.
    """
    # Fetch all Job records from the database
    jobs = Job.objects.all()
    
    # Serialize the queryset (set many=True since we are serializing multiple objects)
    serializer = JobSerializer(jobs, many=True)
    
    # Return the serialized data in the Response
    return Response(serializer.data)
