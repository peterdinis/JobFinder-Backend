from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import JobSerializer, CandidatesAppield
from .models import Job
from django.db.models import Avg, Min, Max, Count
from .filters import JobFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_jobs(request):
    """
    Retrieve all jobs from the database and return them as a serialized JSON response.
    """
    jobs = JobFilter(request.GET, queryset=Job.objects.all().order_by("id"))

    count = jobs.qs.count()
    resPerPage = 3

    paginator = PageNumberPagination()
    paginator.page_size = resPerPage
    queryset = paginator.paginate_queryset(jobs.qs, request)

    serializer = JobSerializer(queryset, many=True)
    return Response({
        "count": count,
        "jobs": serializer.data,
        "resPerPage": resPerPage
    })


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_job(request):
    """
    Create a new job entry in the database.
    """
    request.data["user"] = request.user.id  # Ensure user ID is passed
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_job(request, pk):
    """
    Retrieve a single job by its ID.
    """
    job = get_object_or_404(Job, pk=pk)
    serializer = JobSerializer(job)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def delete_job(request, pk):
    """
    Delete a job by its ID.
    """
    job = get_object_or_404(Job, pk=pk)
    job.delete()
    return Response({"message": "Job deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_topic_stats(request, topic):
    """
    Retrieve statistical data for jobs matching a specific topic in the title.
    """
    args = {"title__icontains": topic}
    jobs = Job.objects.filter(**args)

    if not jobs.exists():
        return Response(
            {"message": f"No stats found for the topic '{topic}'"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    stats = jobs.aggregate(
        total_jobs=Count("id"),
        avg_salary=Avg("salary"),
        min_salary=Min("salary"),
        max_salary=Max("salary")
    )

    return Response({
        "topic": topic,
        "stats": stats,
        "total_jobs": stats["total_jobs"],
        "average_salary": stats["avg_salary"],
        "minimum_salary": stats["min_salary"],
        "maximum_salary": stats["max_salary"]
    })

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def apply_to_job(request, pk):
    """
    Allow a user to apply to a job using a resume.
    """
    job = get_object_or_404(Job, pk=pk)
    user = request.user

    # Check if the user has already applied to this job
    if CandidatesAppield.objects.filter(job=job, user=user).exists():
        return Response(
            {"error": "You have already applied for this job."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Validate resume file or URL from the request
    resume = request.data.get("resume")
    if not resume:
        return Response(
            {"error": "Resume is required to apply for the job."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Save the application
    application = CandidatesAppield.objects.create(job=job, user=user, resume=resume)

    return Response(
        {
            "message": "You have successfully applied to the job.",
            "application_id": application.id,
        },
        status=status.HTTP_201_CREATED,
    )