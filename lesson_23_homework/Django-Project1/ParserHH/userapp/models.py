from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ManyToManyField, CharField

from parserHHapp.models import Area, Schedule

# Create your models here.

class Applicant(AbstractUser):
    text = CharField(max_length=30)
    areas = ManyToManyField(Area)
    schedules = ManyToManyField(Schedule)

