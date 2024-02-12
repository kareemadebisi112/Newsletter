from django import forms
from .models import Email

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']