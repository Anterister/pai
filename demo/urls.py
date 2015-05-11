# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from demo import views

from .views import HomePageView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^demo/', include('demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^$', views.index, name='index'),

    url(r"^r/", include("anafero.urls")),

    url(r'^home/', views.home, name='home'),

    # url(r'^(?P<email_addr_in>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/email_subscribe/$', 
    #     views.email_subscribe, name='email_subscribe'),
    url(r'^email_subscribe/', 
        views.email_subscribe, name='email_subscribe'),

    # url(r'^email_subscribe/$', 
    #     views.email_subscribe_submit, name='email_subscribe_submit'),

    # url(r'^(?P<email_addr_in>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/subscribe_result/$', 
    #     views.email_subscribe_result, name='subscribe_result'),

    url(r'^contact/', views.contact, name='contact'),
    url(r'^FAQ/', views.FAQ, name='FAQ'),

    # These are urls from the subcribe app
    url(r'^subscribe/', include('subscribe.urls')),
    # from members
    url(r'^members/', include('members.urls')),


)
