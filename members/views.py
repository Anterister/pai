# -*- coding: utf-8 -*-  
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

from subscribe.models import SubscriptionForm, Subscription, SubscriptionRecord


from anafero.models import Referral

# def index(request):
# 	return render(request, 'members/attribute.html')

def index(request):
	c = {'member_login_isPOST' : False}
	if (request.method == 'POST'):
		c['member_login_isPOST'] = True
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
			else:
				c['member_login_message'] = "User is not active!"
				# c['login_message'] = "success!"
		else:
			c['member_login_message'] = u"您的用户名和密码不匹配"
	# print request.user.get_profile().referral
	return render(request, 'members/memberIndex.html', c)



def logout_member(request):
	logout(request)
	return HttpResponseRedirect('/members/')
	# return render(request, 'members/index.html')


def register_member(request):
	c = {'member_register_isPOST' : True}
	if (request.method == 'POST'):
		# c['member_login_isPOST'] = True
		email = request.POST['email']

		if User.objects.filter(email = email).exists():
			c['member_register_message'] = u'该邮箱已被注册'
			return render(request, 'members/memberIndex.html', c)			

		password = request.POST['password']

		newUser = User.objects.create_user(email, email, password)
		newUser.save()	

		loginUser = authenticate(username=email, password=password)
		login(request, loginUser)
		return render(request, 'members/confirmation.html');
	else:
		return render(request, 'members/memberIndex.html')



def show_subscriptions(request):
	c = {}
	subscriptions = Subscription.objects.filter(
		subscriber=request.user)
	c['subscriptions_list'] = subscriptions
	return render(request, 'members/subscriptions.html', c)


def subscription_detail(request, subscriptionId):
	c = {}
	subscriptions = Subscription.objects.filter(
		id=subscriptionId)
	if subscriptions:
		subscription = subscriptions[0]
	else:
		return HttpResponseRedirect('/members/subscriptions/')

	if request.user != subscription.subscriber:
		return HttpResponseRedirect('/members/subscriptions/')
	
	return render(request, 'members/subscriptionDetails.html', {'subscription':subscription})


def reset_password(request):
	if (request.method == 'POST'):
		if request.user.check_password(request.POST['old_password']):
			request.user.set_password(request.POST['new_password'])
			request.user.save()
			return render(request, 'members/memberIndex.html', 
				{'resetpwd_msg' : u'修改密码成功！', 'member_resetpwd_isPOST':True}) 
		else:
			return render(request, 'members/memberIndex.html', 
				{'resetpwd_msg' : u'旧密码不正确', 'member_resetpwd_isPOST':True}) 

	return HttpResponseRedirect('/members/')


def refer(request):
	return render(request, 'members/refer.html')


