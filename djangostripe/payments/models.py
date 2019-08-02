from django.db import models
from django.conf import settings
from django.db.models.signals import post_save,pre_save

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

SUBSCRIPTION_CHOICES = (
     ('MONTHLY', 'MONTH'),
    ('YEARLY', 'YEAR'),

)




class Subscription(models.Model):
    subscription_plan = models.CharField(max_length=30,blank=True)
    subscription_type = models.CharField(choices=SUBSCRIPTION_CHOICES,max_length=30,blank=True)
    ammount = models.IntegerField(default=150,blank=True)
    #stripe_subscription_id = models.CharField(max_length=40)
    #email = models.ForeignKey(User,on_delete=models.CASCADE)
   

    def __str__(self):
        return self.subscription_plan

def save_post(sender,instance, **kwargs):
    
    print("something")

post_save.connect(save_post,sender=Subscription)



  
