from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Comment
from payments.views import payments
from .forms import TicketForm, CommentForm
from services import vote_service
from django.contrib.auth.decorators import login_required

@login_required
def all_tickets(request):
    tickets = Ticket.objects.all().order_by('-votes')
    return render(request, "tickets.html", {"tickets": tickets})

@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
           comment = form.save(commit=False)
           comment.ticket_id = ticket.id
           comment.author = request.user.username
           comment.save()
    else:
        form = CommentForm()
    return render(request, 'ticketdetail.html', {'ticket': ticket, 'form':form})

@login_required
def create_or_edit_ticket(request, pk=None):
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if ticket is not None:
        if request.user.username != ticket.created_by:
            return redirect(ticket_detail, ticket.pk)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user.username
            ticket.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticketform.html', {'form': form})  

@login_required
def upvote(request, pk):
    referring_page = request.META['HTTP_REFERER']
    path_list = referring_page.split('/')
    penultimate_index = len(path_list)-2

    ticket = get_object_or_404(Ticket, pk=pk)
    request.session['ticket'] = ticket.id

    if ticket.ticket_type == 'Feature':
        return redirect(payments)
    
    ticket = vote_service.vote(request)

    if path_list[penultimate_index].isnumeric():
        return redirect(ticket_detail, ticket.pk )
    else:
        return redirect(all_tickets)
    




    
                                                 
