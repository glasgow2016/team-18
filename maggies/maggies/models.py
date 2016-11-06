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

class Centre(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }

# NOTE & TODO: Make the naive datetime aware of its timezone
class Visitor(models.Model):
    visit_date_time = models.DateTimeField()
    visit_location = models.ForeignKey(Centre)
    is_new_visitor = models.BooleanField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nature_of_visit = models.ForeignKey(VisitNature)

    def as_dict(self):
        return {
            "id": self.id,
            "visit_date_time": self.visit_date_time,
            "visit_location": self.visit_location.as_dict(),
            "is_new_visitor": self.is_new_visitor,
            "gender": self.gender,
            "nature_of_visit": self.nature_of_visit.pk
        }

class CancerInfo(models.Model):
    cancer_site = models.ForeignKey(CancerSite)
    journey_stage = models.ForeignKey(JourneyStage)

    def as_dict(self):
        return {
            "cancer_site": self.cancer_site.pk,
            "journey_stage": self.journey_stage.pk
        }

class PwC(models.Model):
    visitor = models.OneToOneField(Visitor)
    cancer_info = models.ForeignKey(CancerInfo)

    def as_dict(self):
        return {
            "id": self.id,
            "visitor": self.visitor.as_dict(),
            "cancer_info": self.cancer_info.as_dict()
        }

class Carer(models.Model):
    visitor = models.OneToOneField(Visitor)
    pwc_cancer_info = models.ForeignKey(CancerInfo)
    pwc_present = models.BooleanField()
    caring_for = models.ManyToManyField(PwC, blank = True)
    relationship = models.CharField(max_length=256)

    def as_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "time_first_seen": self.time_first_seen
        }

class OtherVisitor(models.Model):
    visitor = models.OneToOneField(Visitor)
    description = models.CharField(max_length=256)

    def as_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "time_first_seen": self.time_first_seen
        }

# NOTE & TODO: Flush this table every day at, say 02:00
class DailyIdentifier(models.Model):
    first_name = models.CharField(max_length=256)
    time_first_seen = models.DateTimeField()
    visitor = models.OneToOneField(Visitor)

    def as_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "time_first_seen": self.time_first_seen
        }

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
