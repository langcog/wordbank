# from django.conf.urls import patterns, include, url
from django.urls.conf import path
from django.contrib import admin
from django.views.generic import TemplateView

from common.views import *
from instruments.views import *
from . import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("about/", About.as_view(), name="about"),
    path(r"data/", Analyses.as_view(), name="data"),
    path(r"contributors/", Contributors.as_view(), name="contributors"),
    path(r"blog/", Blog.as_view(), name="blog"),
    path(r"faq/", Faq.as_view(), name="faq"),
    path("healthcheck/", views.health_view, name="healthcheck"),
    # connection arguments that wordbankr uses by default
    path(r"db_args/", TemplateView.as_view(template_name="db_args.json"), name="db_args")
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
