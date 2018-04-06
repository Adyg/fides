from django.db import models
from django.utils import timezone


class Breakpoint(models.Model):
    width = models.IntegerField(default=375)
    height = models.IntegerField(default=812)


class Project(models.Model):
    name = models.TextField(blank=False, null=False)
    url = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    breakpoint = models.ForeignKey(Breakpoint, blank=False, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
