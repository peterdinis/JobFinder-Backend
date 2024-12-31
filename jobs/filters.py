from django_filters import rest_framework as filters
from .models import Job

class JobFilter(filters.FilterSet):

    keyword = filters.CharFilter(field_name="title", lookup_expr="icontains")
    location = filters.CharFilter(field_name="address", lookup_expr="icontains")
    min_salary = filters.NumberFilter(field_name="salary", lookup_expr="gte")
    max_salary = filters.NumberFilter(field_name="salary", lookup_expr="lte")
    education = filters.ChoiceFilter(field_name="education", choices=Job.Education.choices)
    job_type = filters.ChoiceFilter(field_name="job_type", choices=Job.JobType.choices)
    experience = filters.ChoiceFilter(field_name="experience", choices=Job.Experience.choices)

    class Meta:
        model = Job
        fields = ("keyword", "location", "education", "job_type", "experience", "min_salary", "max_salary")
