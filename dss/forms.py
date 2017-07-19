from django import forms
from django.apps import apps
from .utility import allorganisms


class InputForm(forms.Form):
	type_of_organisms = forms.ChoiceField(required=False)
	age_group = forms.CharField(required=False, widget=forms.Select())
	system_affected = forms.CharField(required=False, widget=forms.Select())
	organ_affected = forms.CharField(required=False, widget=forms.SelectMultiple())
	causative_agent = forms.CharField(required=False, widget=forms.Select())
	disease_condition = forms.CharField(required=False, widget=forms.Select())
	am_findings = forms.CharField(required=False, widget=forms.SelectMultiple())
	pm_findings = forms.CharField(required=False, widget=forms.SelectMultiple())
	type_of_organisms =  forms.ChoiceField()

	def __init__(self, *args, **kwargs):
		super(InputForm, self).__init__(*args, **kwargs)
		myset =[("","None")]
		for i in allorganisms():
			myset.append((i,i))
		self.fields['type_of_organisms'].choices = myset
