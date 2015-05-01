from django.conf.urls import patterns, include, url

from members import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^logout/', views.logout_member, name='logout'),
	url(r'^register/', views.register_member, name='register'),
	# url(r'^register/form/', views.register_first, name='registerform'),
	url(r'^subscriptions/$', views.show_subscriptions, name='member_subscriptions'),
	url(r'^subscriptions/([0-9]+)/$', views.subscription_detail, name='subscription_detail'),
	url(r'^resetPassword/', views.reset_password, name='reset_password'),
	)