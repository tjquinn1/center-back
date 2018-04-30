from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    account_owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False, max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Project(models.Model):
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    project_name = models.CharField(null=False, blank=False, max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):              # __unicode__ on Python 2
        return self.project_name

class Task(models.Model):
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE)
    task_name = models.CharField(null=False, blank=False, max_length=100)
    created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.task_name

class Time(models.Model):
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)
    time = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=3)
    created = models.DateField(default=timezone.now)
    non_billable = models.BooleanField(default=False)