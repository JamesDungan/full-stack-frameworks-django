import stripe

from django.shortcuts import render
from django.conf import settings
from IssueTracker.globe import vote
from django.views.generic.base import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY

def payments(request):
    key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'payments.html', {'key':key})

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='eur',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')