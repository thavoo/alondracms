from django import forms

class EmailForm(forms.Form):
	q = forms.EmailField(max_length=255)
