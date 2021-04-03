# from django.conf.urls import patterns, include, url
from django.conf.urls import url
from django.urls.conf import path
from django.contrib import admin


from common.views import *
from instruments.views import *
from . import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = urlpatterns = [
    # Examples:
    path('admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name='home'),
    url(r'about', About.as_view(), name='about'),
    url(r'analyses', Analyses.as_view(), name='analyses'),
    url(r'contributors', Contributors.as_view(), name='contributors'),
    url(r'publications', Publications.as_view(), name='publications'),
    url(r'stats', Stats.as_view(), name='stats'),
    url(r'blog', Blog.as_view(), name='blog'),
    url(r'faq', Faq.as_view(), name='faq'),
    path('healthcheck/', views.health_view, name="healthcheck" )

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
