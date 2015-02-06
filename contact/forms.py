__author__ = 'raman'

from django.db import models
from contact.models import EmailForm
from django import forms
class EmailForm(forms.Form):
      firstname = forms.CharField(max_length=255)
      lastname = forms.CharField(max_length=255)
      email = forms.EmailField()
      subject = forms.CharField(max_length=255)
      botcheck = forms.CharField(max_length=5)
      message = forms.CharField(max_length=600)
class ContactForm(forms.Form):
    name = forms.CharField(help_text="Your name...")
    email = forms.EmailField(help_text="Your email ...",required=True)
    message = forms.CharField(widget=forms.Textarea,required=True)
