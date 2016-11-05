from django import models

MALE = 'M'
FEMALE = 'F'
OTHER = 'O'
GENDER_CHOICES = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
)

class Visitor(models.Model):
    is_new_visitor = models.BooleanField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    cancer_site = models.ForeignKey(CancerSite)
    nature_of_visit = models.ForeignKey(VisitNature)

class DailyIdentifier(models.Model):
    first_name = models.CharField()
    visitor = models.OneToOneField(Visitor)

class CancerSite(models.Model):
    name = models.CharField(max_length=256)

class VisitNature(models.Model):
    nature = models.CharField(max_length=256)

class JourneyStage(models.Model):
    stage = models.CharField(max_length=256)
