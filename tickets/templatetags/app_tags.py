from django import template
from .models import Vote

register = template.Library()

@register.assignment_tag
# def user_voted_tag():