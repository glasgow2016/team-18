from django import forms

class VisitorForm(forms.Form):
    visitor_name = forms.CharField(label="Visitor's name", max_length=100)
