from django import forms

class FlowerForm(forms.Form):
	genus = forms.CharField(max_length=30)
	species = forms.CharField(max_length=30)
	comname = forms.CharField(max_length=30)


class SightingForm(forms.Form):
	name = forms.CharField(max_length=30)
	person = forms.CharField(max_length=30)
	location = forms.CharField(max_length=30)

	year = forms.CharField(max_length=4)
	month = forms.CharField(max_length=2)
	day = forms.CharField(max_length=2)

	# sighted = forms.CharField(max_length=30)