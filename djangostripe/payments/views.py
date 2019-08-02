# payments/views.py
import stripe # new

from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render # new

stripe.api_key = settings.STRIPE_SECRET_KEY # new


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=15000,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        print(charge, "hello")
        plan = stripe.Plan.create(
  currency='gbp',
  interval='month',
  product='prod_FUebirlx6N99Rp',
  nickname='Pro Plan',
  amount=3000,
)
        return render(request, 'charge.html')