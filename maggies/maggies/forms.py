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
    visitor_name = forms.CharField(label="Visitor's First Name", max_length=100, help_text="This will help identify this person on their travels today only.")
    visitor_type = forms.ChoiceField(choices=VISITOR_TYPE_CHOICES, label="Visitor Type")
    is_new_visitor = forms.BooleanField(required=False, label="First visit?", help_text="Was this their first visit?")
    visitor_gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender")
    nature_of_visit = forms.ModelChoiceField(VisitNature.objects.all(), label="Nature of Visit", help_text="How did the person visit the centre today? (e.g. did they have an appointment or just drop in?)")
    cancer_site = forms.ModelChoiceField(CancerSite.objects.all(), label="Cancer Site", help_text="Where is the site of the person's cancer? Select 'Not Stated' if it did not come up in conversation, or 'Unknown Primary' if even their doctor doesn't know.")
    journey_stage = forms.ModelChoiceField(JourneyStage.objects.all(), label="Journey Stage")

    # Secret hidden fields used for tracking
    has_been_seen_today = forms.BooleanField(required=False, label="Has Been Seen Today")
    dailyid_id = forms.IntegerField(required=False, label="DailyIdentifier ID")

class ReportsForm(forms.Form):
    report_timeframe = forms.ChoiceField(choices=REPORTS_TIMEFRAME_CHOICES, label="Report Timeframe")
