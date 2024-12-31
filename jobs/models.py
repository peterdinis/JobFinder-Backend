from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone 

def return_date_time():
    return timezone.now()

class JobType(models.TextChoices):
    Permanent = "Permanent"
    Temporary = "Temporary"
    Intership = "Intership"

class Education(models.TextChoices):
    Bachelor = "Bachelor"
    Master =  "Master"
    Phd = "Phd"

class Industry(models.TextChoices):
    Business = "Business"
    IT = "IT"
    Banking = "Banking"
    Education = "Education"
    Others = "Others"

class Experience(models.TextChoices):
    NO_EXPERIENCE = "No Experience"
    ONE_YEAR = "1 Year"
    TWO_YEAR = "2 Years"
    THREE_YEAR_PLUS = "3 Years above"

class Job(models.Model):
    title = models.CharField(max_length=200, null=True, default="")
    description = models.TextField(max_length=1000, null=True, default="")
    email = models.EmailField(max_length=100, default=True, null=True)
    address = models.CharField(max_length=200, default=True, null=True)
    salary = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    experience = models.CharField(max_length=20, choices=Experience.choices, default=Experience.THREE_YEAR_PLUS)
    industry = models.CharField(max_length=20, choices=Industry.choices, default=Industry.IT)
    job_type = models.CharField(max_length=20, choices=JobType.choices, default=JobType.Permanent)
    education = models.CharField(max_length=20, choices=Education.choices, default=Education.Bachelor)
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True, default="")
    last_date = models.DateTimeField(default=return_date_time)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    jobLocation = models.TextField(max_length=300, default="")
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
