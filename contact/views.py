from django.shortcuts import render

# Create your views here.
from django.utils import simplejson
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from contact.forms import ContactForm
from forms import EmailForm
def sendmail(request):
      if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
          firstname = form.cleaned_data['firstname']
          lastname = form.cleaned_data['lastname']
          email = form.cleaned_data['email']
          subject = form.cleaned_data['subject']
          botcheck = form.cleaned_data['botcheck'].lower()
          message = form.cleaned_data['message']

          if botcheck == 'yes':
            try:
              fullemail = firstname + " " + lastname + " " + "<" + email + ">" + " "
              send_mail(subject, message, fullemail, ['raman.kumar@nescode.com'])
              return HttpResponseRedirect('/email/thankyou/')
            except:
              return HttpResponseRedirect('/email/')
        else:
          return HttpResponseRedirect('/email/')
      else:
        return HttpResponseRedirect('/email/')



