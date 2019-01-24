from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Comment

def all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets.html", {"tickets": tickets})

def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'ticketdetail.html', {'ticket': ticket})