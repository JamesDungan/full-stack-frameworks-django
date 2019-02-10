from django import forms
from .models import Ticket, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text' : forms.Textarea(attrs={'rows':2,'cols':20}),
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'text', 'ticket_type']
