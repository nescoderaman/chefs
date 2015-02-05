from django.contrib.auth.views import password_reset
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

__author__ = 'raman'

def success_password(request):
    return HttpResponseRedirect('/complete',)

def check(request):
    return password_reset(request, template_name='check.html',
        post_reset_redirect=reverse('success'))