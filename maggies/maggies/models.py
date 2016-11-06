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

    def __str__(self):
        return self.nature

class CancerSite(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class JourneyStage(models.Model):
    stage = models.CharField(max_length=256)

    def __str__(self):
        return self.stage

class Visitor(models.Model):
    visit_date = models.DateField()
    is_new_visitor = models.BooleanField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nature_of_visit = models.ForeignKey(VisitNature)

class CancerInfo(models.Model):
    cancer_site = models.ForeignKey(CancerSite)
    journey_stage = models.ForeignKey(JourneyStage)

class PwC(models.Model):
    visitor = models.OneToOneField(Visitor)
    cancer_info = models.ForeignKey(CancerInfo)

class Carer(models.Model):
    visitor = models.OneToOneField(Visitor)
    pwc_cancer_info = models.ForeignKey(CancerInfo)
    pwc_present = models.BooleanField()
    caring_for = models.ManyToManyField(PwC, blank = True)
    relationship = models.CharField(max_length=256)

class OtherVisitor(models.Model):
    visitor = models.OneToOneField(Visitor)
    description = models.CharField(max_length=256)

# NOTE & TODO: Flush this table every day at, say 02:00
class DailyIdentifier(models.Model):
    first_name = models.CharField(max_length=256)
    time_first_seen = models.DateTimeField()
    visitor = models.OneToOneField(Visitor)

class Centre(models.Model):
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
    work_location = models.ManyToManyField(Centre)
    clearance_level = models.ForeignKey(ClearanceLevel)
    assisted = models.ManyToManyField(Visitor)

class Activity(models.Model):
    name = models.CharField(max_length=256)
    location = models.ManyToManyField(Centre)
    participants = models.ManyToManyField(Visitor)
    coordinators = models.ManyToManyField(StaffMember)
    class Meta:
        verbose_name_plural = "activities"

class KnownVisitors(models.Model):
    first_name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=256)
    notes = models.CharField(max_length=256)
