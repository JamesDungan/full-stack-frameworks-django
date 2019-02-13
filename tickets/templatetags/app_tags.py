from django import template
from tickets.models import Vote
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.simple_tag
def user_voted_tag(ticket, user):
    try:
        vote = Vote.objects.get(ticket=ticket, username=user)
    except ObjectDoesNotExist:
        vote = None
    if vote:
        return True
    else:
        return False

@register.simple_tag
def ticket_owner_tag(ticket, user):
    if ticket.created_by == user:
        return True
    else:
        return False
