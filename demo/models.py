from django.db import models
from django.forms import ModelForm

class EmailSubscriber(models.Model):
	email_addr = models.EmailField(primary_key=True)
	dog_name = models.CharField(max_length=30)
	dog_birthday = models.DateField(null=True,blank=True)

	def __unicode__(self):
		return self.email_addr


class EmailSubscriberForm(ModelForm):
    class Meta:
        model = EmailSubscriber
        fields = ['email_addr']

