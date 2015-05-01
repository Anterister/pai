# -*- coding: utf-8 -*-  
from django.shortcuts import render
from subscribe.models import SubscriptionForm, Subscription, SubscriptionRecord
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	return render(request, 'subscribe/index.html')


def plan(request, size):
	return render(request, 'subscribe/plan.html')

def summary(request, size, plan):
	c = {'member_login_isPOST' : False}

	c['subscribe_form'] = SubscriptionForm()
	if (size == 'S'):
		c['dog_size'] = u'小型犬'
	elif (size == 'M'):
		c['dog_size'] = u'中型犬'
	elif (size == 'L'):
		c['dog_size'] = u'大型犬'

	if plan == '1':
		c['subscribe_plan'] = u'一个月'
	elif plan == '3':
		c['subscribe_plan'] = u'三个月'
	elif plan == '6':
		c['subscribe_plan'] = u'六个月'

		# c['dog_size'] = request.POST
	c['subscribe_price'] = 68

	if (request.method == 'POST'):

		if request.POST['postType'] == "login":
			c['member_login_isPOST'] = True
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
				else:
					c['member_login_message'] = u"出错了，请稍后再试..."
					# c['login_message'] = "success!"
			else:
				c['member_login_message'] = u"您的用户名和密码不匹配."

		elif request.POST['postType'] == "signup":
			c['member_register_isPOST'] = True
			email = request.POST['email']
			if User.objects.filter(email = email).exists():
				c['member_register_message'] = u'该邮箱已被注册'
			else:
				password = request.POST['password']

				newUser = User.objects.create_user(email, email, password)
				newUser.save()	

				# TODO: send WELCOME email!!!!
				c['has_feedback_message'] = True
				c['feedback_message'] = u'注册成功！我们已将一封欢迎邮件发送至您的邮箱。'

				loginUser = authenticate(username=email, password=password)
				login(request, loginUser)
			
		elif request.POST['postType'] == "forgetPassword":

			c['has_feedback_message'] = True
			username = request.POST['forgetEmail']
			if User.objects.filter(email = username).exists():
				c['feedback_message'] = u"我们已经将一封重置密码的邮件发送至您的邮箱，请注意查收！"
				# TODO: send reset password email!!!!
			else:
				c['feedback_message'] = u"该邮箱未被注册，请重新输入。"

			

	return render(request, 'subscribe/summary.html', c)



def submit(request, size, plan):
	# if user not logged in, return to summary page
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/subscribe/%s/%s/" % (size, plan))
	
	c = {}
	if (request.method == 'POST'):

		# print request.POST

		new_subscription = Subscription(
			subscriber=request.user,
			subscription_size=size,
			subscription_plan=plan,
			# pet_name=pet_name_in,
			# pet_birthday=pet_birthday_in,
			# pet_gender=pet_gender_in,
			# pet_breed=pet_breed_in,
			s_name=request.POST['s_name'],
			s_phonenumber=request.POST['s_phonenumber'],
			s_address=request.POST['s_address'],
			s_city=request.POST['s_city'],
			s_province=request.POST['s_province'],
			s_zipcode=request.POST['s_zipcode'],
			s_note=request.POST['s_note'],
			)

		# pet_name_in = ""
		# pet_gender_in = ""
		# pet_birthday_in = "1900-1-1"
		# pet_breed_in = ""

		if request.POST['pet_name']:
			new_subscription.pet_name = request.POST['pet_name']
		if request.POST['pet_gender']:
			new_subscription.pet_gender = request.POST['pet_gender']
		if request.POST['pet_birthday']:
			mmddyyyy = request.POST['pet_birthday'].split('/')
			# print "%s-%s-%s" % (mmddyyyy[2], mmddyyyy[0], mmddyyyy[1])
			new_subscription.pet_birthday = "%s-%s-%s" % (mmddyyyy[2], mmddyyyy[0], mmddyyyy[1])
		if request.POST['pet_breed']:
			if request.POST['pet_breed'] == '0':				
				new_subscription.pet_breed = request.POST['pet_breed_type']
			else:
				new_subscription.pet_breed = request.POST['pet_breed']

		new_subscription.save()

		new_subscription_record = SubscriptionRecord(
			order_id=new_subscription.id)
		new_subscription_record.save()

		

	return render(request, 'subscribe/confirmation.html', c)