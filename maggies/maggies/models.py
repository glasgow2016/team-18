from django.db import models

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

class CancerSite(models.Model):
    name = models.CharField(max_length=256)

class JourneyStage(models.Model):
    stage = models.CharField(max_length=256)

class Visitor(models.Model):
    is_new_visitor = models.BooleanField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nature_of_visit = models.ForeignKey(VisitNature)

class PwC(Visitor):
    cancer_site = models.ForeignKey(CancerSite)
    journey_stage = models.ForeignKey(JourneyStage)

class Carer(Visitor):
    caring_for = models.ForeignKey(PwC)
    relationship = models.CharField(max_length=256)

class OtherVisitor(Visitor):
    description = models.CharField(max_length=256)

# NOTE & TODO: Flush this table every day at, say 02:00
class DailyIdentifier(models.Model):
    first_name = models.CharField(max_length=256)
    time_first_seen = models.DateTimeField()
    visitor = models.OneToOneField(Visitor)

class StaffRole(models.Model):
    description = models.CharField(max_length=256)

class StaffMember(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    account_id = models.IntegerField(unique=True)
    role = models.ForeignKey(StaffRole, on_delete=models.PROTECT)
    assisted = models.ManyToManyField(Visitor)

class Activity(models.Model):
    name = models.CharField(max_length=256)
    time = models.DateTimeField()
    location = models.CharField(max_length=256)
    participants = models.ManyToManyField(Visitor)
    coordinators = models.ManyToManyField(StaffMember)
