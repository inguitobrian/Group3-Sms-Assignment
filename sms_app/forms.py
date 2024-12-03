# sms_app/forms.py
from django import forms

class SMSForm(forms.Form):
    to_number = forms.CharField(label='Phone Number', max_length=15)
    message_body = forms.CharField(label='Message', widget=forms.Textarea)
