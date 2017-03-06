from django import forms
class ContactForm(forms.Form):
    name=forms.CharField(required=True)
    company = forms.CharField(required=False)
    email=forms.CharField(required=True)
    telephone=forms.CharField(required=False)
    message=forms.CharField(required=True,widget=forms.Textarea)