from django.conf.urls import patterns, include, url
from common.views import *
from instruments.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Home.as_view(), name='home'),
    url(r'about', About.as_view(), name='about'),
    url(r'stats', Stats.as_view(), name='stats'),
    url(r'reports', Reports.as_view(), name='reports'),
    url(r'contribute', Contribute.as_view(), name='contribute'),
    url(r'blog', Blog.as_view(), name='blog'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
