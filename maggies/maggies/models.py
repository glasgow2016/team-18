from django.db import models

class StaffMember(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    description = models.ForeignKey(StaffDescription, on_delete=models.PROTECT)

class StaffDescription(models.Model):
    description = models.CharField(max_length=256)

class Activity(models.Model):
    name = models.CharField(max_length=256)
    time = models.DateTimeField()
    location = models.CharField(max_length=256)
    participants = models.ManyToManyField(Visitor)
    coordinators = models.ManyToManyField(StaffMember)