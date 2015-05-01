from django.contrib import admin
# from subscribe.models import BoxSubscriber, SubscribingPet, SubscribingSession
from subscribe.models import Subscription, SubscriptionRecord

# Register your models here.
admin.site.register(Subscription)
admin.site.register(SubscriptionRecord)
# admin.site.register(SubscribingPet)
# admin.site.register(SubscribingSession)
