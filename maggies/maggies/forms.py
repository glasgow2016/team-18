from django import forms
from .models import VisitNature, CancerSite, JourneyStage, MALE, FEMALE, OTHER, GENDER_CHOICES

PWC = "PWC"
CARER = "CAR"
OTHER = "OTH"
DAY = "DAY"
WEEK = "WEEK"
MONTH = "MONTH"
YEAR = "YEAR"

VISITOR_TYPE_CHOICES = (
    (PWC, 'Person with Cancer'),
    (CARER, 'Carer'),
    (OTHER, 'Other'),
)

REPORTS_TIMEFRAME_CHOICES = (
    (DAY, "Day"),
    (WEEK, "Week"),
    (MONTH, "Month"),
    (YEAR, "Year"),
)

class VisitorForm(forms.Form):
    visitor_name = forms.CharField(label="Visitor's First Name", max_length=100)
    visitor_type = forms.ChoiceField(choices=VISITOR_TYPE_CHOICES, label="Visitor Type")
    is_new_visitor = forms.BooleanField(label="First visit?")
    visitor_gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender")
    nature_of_visit = forms.ModelChoiceField(VisitNature.objects.all(), label="Nature of Visit")
    cancer_site = forms.ModelChoiceField(CancerSite.objects.all(), label="Cancer Site")
    journey_stage = forms.ModelChoiceField(JourneyStage.objects.all(), label="Journey Stage")

class ReportsForm(forms.Form):
    report_timeframe = forms.ChoiceField(choices=REPORTS_TIMEFRAME_CHOICES, label="Report Timeframe")
