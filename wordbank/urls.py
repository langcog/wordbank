from django.conf.urls import patterns, include, url
from common.views import *
from instruments.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Home.as_view(), name='home'),
    url(r'analyses', Analyses.as_view(), name='analyses'),
    url(r'contributors', Contributors.as_view(), name='contributors'),
    url(r'publications', Publications.as_view(), name='publications'),
    url(r'stats', Stats.as_view(), name='stats'),
    url(r'blog', Blog.as_view(), name='blog'),
    url(r'faq', Faq.as_view(), name='faq'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
