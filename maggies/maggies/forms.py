from django import forms
from .models import VisitNature, CancerSite, JourneyStage

class VisitorForm(forms.Form):
    visitor_name = forms.CharField(label="Visitor's First Name", max_length=100)
    visitor_type = forms.ChoiceField(label="Visitor Type")
    is_new_visitor = forms.BooleanField(label="First visit?")
    visitor_gender = forms.ChoiceField(label="Gender")
    nature_of_visit = forms.ModelChoiceField(VisitNature.objects.all(), label="Nature of Visit")
    cancer_site = forms.ModelChoiceField(CancerSite.objects.all(), label="Cancer Site")
    journey_stage = forms.ModelChoiceField(JourneyStage.objects.all(), label="Journey Stage")
