from django import forms

class DemoForm(forms.Form):
    content = forms.CharField(max_length=1000,blank=False)
