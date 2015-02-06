from django.db import models
from django import forms
from django.utils import simplejson
from django.http import HttpResponse
from django.core.mail import EmailMessage

# Create your models here.
from django.db import models
from django import forms
class EmailForm(models.Model):
      firstname = models.CharField(max_length=255)
      lastname = models.CharField(max_length=255)
      email = models.EmailField()
      subject = models.CharField(max_length=255)
      botcheck = models.CharField(max_length=5)
      message = models.CharField(max_length=600)

