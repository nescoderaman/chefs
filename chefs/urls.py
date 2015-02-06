from __future__ import print_function
from cms.sitemaps import CMSSitemap
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings



from django.views.generic.base import TemplateView
from contact.forms import ContactForm
from contact.views import sendmail
from views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^success/$','chefs.views.success_password',name="success"),
        url(r'^contact-us/$', 'chefs.views.check', name='check'),
        url(r'^email/send/$', sendmail),
        url(r'^email/thankyou/$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
        url(r'^email/$', TemplateView.as_view(template_name='check.html'), name='check'),

        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
