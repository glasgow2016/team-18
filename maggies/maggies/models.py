from django.db import models

MALE = 'M'
FEMALE = 'F'
OTHER = 'O'
GENDER_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
)

class CancerSite(models.Model):
    name = models.CharField(max_length=256)

class VisitNature(models.Model):
    nature = models.CharField(max_length=256)

class JourneyStage(models.Model):
    stage = models.CharField(max_length=256)

class Visitor(models.Model):
    is_new_visitor = models.BooleanField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    cancer_site = models.ForeignKey(CancerSite)
    nature_of_visit = models.ForeignKey(VisitNature)
    journey_stage = models.ForeignKey(JourneyStage)

class DailyIdentifier(models.Model):
    first_name = models.CharField(max_length=256)
    time_first_seen = models.DateTimeField()
    visitor = models.OneToOneField(Visitor)

class StaffDescription(models.Model):
    description = models.CharField(max_length=256)

class StaffMember(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    description = models.ForeignKey(StaffDescription, on_delete=models.PROTECT)

class Activity(models.Model):
    name = models.CharField(max_length=256)
    time = models.DateTimeField()
    location = models.CharField(max_length=256)
    participants = models.ManyToManyField(Visitor)
    coordinators = models.ManyToManyField(StaffMember)
