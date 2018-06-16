from django import forms

class RateForm(forms.Form):
	rating = forms.IntegerField()
