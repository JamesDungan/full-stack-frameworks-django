from django import forms
from .models import Ticket, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'text', 'ticket_type', 'created_by']
