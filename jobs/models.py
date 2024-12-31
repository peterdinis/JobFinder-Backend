from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point

class JobType(models.TextChoices):
    Permanent = "Permanent"
    Temporary = "Temporary"
    Intership = "Intership"

class Education(models.TextChoices):
    Bachelor = "Bachelor"
    Maser =  "Master"
    Phd = "Phd"

class Industry(models.TextChoices):
    Busniess = "Busniess"
    IT = "IT"
    Banking = "Banking"
    Education = "Education"
    Others = "Others"

class Expirience(models.TextChoices):
    NO_EXPIRIENCE = "No Expirience"
    ONE_YEAR = "1 Year"
    TWO_YEAR = "2 Year"
    THREE_YEAR_PLUS = "3 Years above"

class Job(models.Model):
    title = models.CharField(max_length=200, null=True, default="")
    description = models.TextField(max_length=1000, null=True, default="")
    email = models.EmailField(max_length=100, default=True, null=True)
    address = models.CharField(max_length=200, default=True, null=True)
    salary = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    expirience = models.CharField(max_length=10, choices=Expirience.choices, default=Expirience.THREE_YEAR_PLUS)
    indrusty = models.CharField(max_length=10, choices=Industry.choices, default=Industry.IT)
    jobType = models.CharField(max_length=10, choices=JobType.choices, default=JobType.Permanent)
    eductation = models.CharField(max_length=10, choices=Education.choices, default=Education.Bachelor)
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True, default="")
    point = gismodels.PointField(default=Point(0.0, 0.0))

    