import stripe
from django.shortcuts import render
from django.conf import settings
from services import vote_service
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def payments(request):
    key = settings.STRIPE_PUBLISHABLE_KEY
    ticket = vote_service.get_ticket(request)
    return render(request, 'payments.html', {'key':key, 'ticket':ticket})

@login_required
def charge(request):
    if request.method == 'POST':
        ticket_id =  request.session['ticket']

        charge = stripe.Charge.create(
            amount=500,
            currency='eur',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        ticket = vote_service.vote(request)
        return render(request, 'charge.html', {'ticket':ticket})