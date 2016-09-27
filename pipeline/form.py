from django import forms

class DemoForm(forms.Form):
	content = forms.CharField(max_length=1000)

class ConsultForm(forms.Form):
	user = forms.CharField(max_length=20)
	email = forms.EmailField(max_length=30)
	message = forms.CharField(max_length=200)
