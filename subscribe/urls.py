from django.conf.urls import patterns, include, url

from subscribe import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(S|M|L)/$', views.plan, name='plan'),
	url(r'^(S|M|L)/(1|3|6)/$', views.summary, name='summary'),
	url(r'^(S|M|L)/(1|3|6)/submit/$', views.submit, name='submit'),
	)