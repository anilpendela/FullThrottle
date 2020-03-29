from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class ActivityPeriods(models.Model):
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False)

class User(AbstractBaseUser):
    user_id = models.CharField(max_length=16, null=True, blank=True)
    tz = models.CharField(max_length=64, null=True, blank=True)
    real_name = models.CharField(max_length=64, null=True, blank=True)
    activity_periods = models.ManyToManyField(to=ActivityPeriods)