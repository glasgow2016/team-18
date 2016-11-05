from django.db import models
from django.contrib.auth.models import User

MALE = 'M'
FEMALE = 'F'
OTHER = 'O'
GENDER_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
)

class VisitNature(models.Model):
    nature = models.CharField(max_length=256)

    def __unicode__():
        return nature

class CancerSite(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__():
        return name

class JourneyStage(models.Model):
    stage = models.CharField(max_length=256)

    def __unicode__():
        return stage

class Visitor(models.Model):
    is_new_visitor = models.BooleanField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nature_of_visit = models.ForeignKey(VisitNature)

class CancerInfo(models.Model):
    cancer_site = models.ForeignKey(CancerSite)
    journey_stage = models.ForeignKey(JourneyStage)

class PwC(Visitor):
    cancer_info = models.ForeignKey(CancerInfo)

class Carer(Visitor):
    pwc_cancer_info = models.ForeignKey(CancerInfo)
    pwc_present = models.BooleanField()
    caring_for = models.ManyToManyField(PwC)
    relationship = models.CharField(max_length=256)

class OtherVisitor(Visitor):
    description = models.CharField(max_length=256)

# NOTE & TODO: Flush this table every day at, say 02:00
class DailyIdentifier(models.Model):
    first_name = models.CharField(max_length=256)
    time_first_seen = models.DateTimeField()
    visitor = models.OneToOneField(Visitor)

class Location(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

class StaffRole(models.Model):
    description = models.CharField(max_length=256)

class ClearanceLevel(models.Model):
    value = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

class StaffMember(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    role = models.ForeignKey(StaffRole, on_delete=models.PROTECT)
    work_location = models.ManyToManyField(Location)
    clearance_level = models.ForeignKey(ClearanceLevel)
    assisted = models.ManyToManyField(Visitor)

class Activity(models.Model):
    name = models.CharField(max_length=256)
    time = models.DateTimeField()
    location = models.ManyToManyField(Location)
    participants = models.ManyToManyField(Visitor)
    coordinators = models.ManyToManyField(StaffMember)
