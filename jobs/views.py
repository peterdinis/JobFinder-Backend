from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import JobSerializer
from .models import Job

@api_view(["GET"])
def get_all_jobs(request):
    """
    Retrieve all jobs from the database and return them as a serialized JSON response.
    """
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_job(request):
    """
    Create a new job entry in the database.
    """
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_job(request, pk):
    """
    Retrieve a single job by its ID.
    """
    job = get_object_or_404(Job, pk=pk)
    serializer = JobSerializer(job)
    return Response(serializer.data)

@api_view(["PUT", "PATCH"])
def update_job(request, pk):
    """
    Update an existing job by its ID.
    """
    job = get_object_or_404(Job, pk=pk)
    serializer = JobSerializer(job, data=request.data, partial=("PATCH" in request.method))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_job(request, pk):
    """
    Delete a job by its ID.
    """
    job = get_object_or_404(Job, pk=pk)
    job.delete()
    return Response({"message": "Job deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
