from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Comment
from .forms import TicketForm, CommentForm

def all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets.html", {"tickets": tickets})

def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
           comment = form.save(commit=False)
           comment.ticket_id = ticket.id
           comment.save()
    else:
        form = CommentForm()
    return render(request, 'ticketdetail.html', {'ticket': ticket, 'form':form})

def create_or_edit_ticket(request, pk=None):
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticketform.html', {'form': form})  

def upvote(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.votes += 1
    ticket.save()
    
    referring_page = request.META['HTTP_REFERER']
    path_list = referring_page.split('/')
    penultimate_index = len(path_list)-2 
        
    if path_list[penultimate_index].isnumeric():
        return redirect(ticket_detail, ticket.pk )
    else:
        return redirect(all_tickets)
    
                                                 
