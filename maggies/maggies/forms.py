from django import forms
from .models import VisitNature, CancerSite, JourneyStage, MALE, FEMALE, OTHER, GENDER_CHOICES, Activity

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

class ActivityForm(forms.Form):
    activity_name = forms.ModelChoiceField(Activity.objects.all(), label="Activity")

class VisitorForm(forms.Form):
    visitor_name = forms.CharField(label="Visitor's First Name", max_length=100)
    visitor_type = forms.ChoiceField(choices=VISITOR_TYPE_CHOICES, label="Visitor Type")
    is_new_visitor = forms.BooleanField(required=False, label="First visit?")
    has_been_seen_today = forms.BooleanField(required=False, label="Has Been Seen Today")
    dailyid_id = forms.IntegerField(required=False, label="DailyIdentifier ID")
    visitor_gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender")
    nature_of_visit = forms.ModelChoiceField(VisitNature.objects.all(), label="Nature of Visit")
    cancer_site = forms.ModelChoiceField(CancerSite.objects.all(), label="Cancer Site")
    journey_stage = forms.ModelChoiceField(JourneyStage.objects.all(), label="Journey Stage")

class ReportsForm(forms.Form):
    report_timeframe = forms.ChoiceField(choices=REPORTS_TIMEFRAME_CHOICES, label="Report Timeframe")
