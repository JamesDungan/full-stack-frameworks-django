from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from tickets.models import Ticket, Vote


def get_ticket(request):
    ticket_id = request.session['ticket']
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return ticket

def vote(request):
    ticket = get_ticket(request)
    user = User.objects.get(username=request.user.username) 
    vote = Vote(username=user, ticket=ticket)
    vote.save()
    ticket.votes += 1
    ticket.save()
    
    return ticket