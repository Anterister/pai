from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from anafero.models import Referral

from django.db.models.signals import post_save




class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True)

	# Other fields here
	email_confirmed = models.BooleanField(default=False)
	being_referred = models.BooleanField(default=False)
	total_referrals = models.IntegerField(default=0)
	avail_free_boxes = models.IntegerField(default=0)

	referral = models.OneToOneField(Referral,default=None)

    # TODO: add my dogs maybe??

# create user profile function???
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		referral = Referral.create(
			user=instance,
			redirect_to="/subscribe/"
			)
		UserProfile.objects.create(user=instance,referral=referral)

post_save.connect(create_user_profile, sender=User)


class Subscription(models.Model):
	# PK is order number, automatic field??
	# order_number = models.EmailField(primary_key=True)

	subscriber = models.ForeignKey(User)
	is_gift = models.BooleanField(default=False)

	# size
	SIZE_CHOICES = (
		('S', 'Small'), 
		('M', 'Midium'),
		('L', "Large"),
		('X', "Extra"),
		)
	subscription_size = models.CharField(max_length=1, 
		choices=SIZE_CHOICES)

	# plan
	SUBSCRIPTION_PLAN_CHOICES = (
		('1', 'OneMonth'),
		('3', 'ThreeMonths'),
		('6', 'SixMonths'),
		('12', 'OneYear'),
		)
	subscription_plan = models.CharField(max_length=1, 
		choices=SUBSCRIPTION_PLAN_CHOICES)

	###########
	# DOG
	###########
	pet_name = models.CharField(max_length=30)
	pet_birthday = models.DateField(null=True, blank=True)

	GENDER_CHOICES = (
		('1', 'Male'), 
		('0', 'Female'),
		)
	pet_gender = models.CharField(max_length=1, 
		choices=GENDER_CHOICES)

	pet_breed = models.CharField(max_length=30)


	###########
	# CONTACT
	###########
	s_phonenumber = models.CharField(max_length=20)
	s_name = models.CharField(max_length=20)

	# TODO: or use a full pre-defined list for trial?
	s_address = models.CharField(max_length=50)
	s_zipcode = models.CharField(max_length=15)
	s_district = models.CharField(max_length=15)
	s_city = models.CharField(max_length=15)
	s_province = models.CharField(max_length=15)
	s_note = models.CharField(max_length=50)


class SubscriptionRecord(models.Model):
	order_id = models.IntegerField(primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True)

	paid_at = models.DateField(null=True, blank=True)
	dispatched_at = models.DateField(null=True, blank=True)

	tracking_info = models.CharField(max_length=50)



# class SubscribingSession(models.Model):
# 	subscriber = models.ForeignKey('BoxSubscriber')
# 	DURATION_CHOICES = (
# 		('1', 'OneMonth'),
# 		('3', 'ThreeMonths'),
# 		('6', 'SixMonths'),
# 		('12', 'OneYear'),
# 		)
# 	subcribing_duration = models.CharField(max_length=1, choices=DURATION_CHOICES)

# class BoxSubscriber(models.Model):
# 	login_email = models.EmailField(primary_key=True)
# 	login_pswd = models.CharField(max_length=50)

# 	s_phonenumber = models.CharField(max_length=20)
# 	s_name = models.CharField(max_length=20)

# 	# TODO: or use a full pre-defined list for trial?
# 	s_address = models.CharField(max_length=50)
# 	s_zipcode = models.CharField(max_length=15)
# 	s_district = models.CharField(max_length=15)
# 	s_city = models.CharField(max_length=15)
# 	s_province = models.CharField(max_length=15)
# 	s_note = models.CharField(max_length=50)


# 	s_pet = models.ForeignKey('SubscribingPet')

# class SubscribingPet(models.Model):
# 	pet_name = models.CharField(max_length=30)
# 	pet_birthday = models.DateField(null=True, blank=True)
# 	GENDER_CHOICES = (
# 		('M', 'Male'), 
# 		('F', 'Female'),
# 		('O', "Other")
# 		)
# 	pet_gender = models.CharField(max_length=1, 
# 		choices=GENDER_CHOICES)

# 	SIZE_CHOICES = (
# 		('S', 'Small'), 
# 		('M', 'Midium'),
# 		('L', "Large"),
# 		('X', "Extra"),
# 		)
# 	pet_size = models.CharField(max_length=1, 
# 		choices=SIZE_CHOICES)

class SubscriptionForm(ModelForm):
	class Meta:
		model = Subscription
		fields= {"pet_name", "pet_birthday", "pet_gender",
		"s_name", "s_phonenumber",
		"s_address", "s_district", "s_city", "s_province", "s_zipcode",
		}


# class BoxSubscriberForm(ModelForm):
# 	class Meta:
# 		model = BoxSubscriber
# 		fields = {'login_email', 'login_pswd'}
