from django.urls import path, include
from django.conf.urls import url
from .views import all_tickets, ticket_detail, create_or_edit_ticket, upvote

urlpatterns = [
    path('', all_tickets, name='tickets'),
    url(r'^(?P<pk>\d+)/$', ticket_detail, name='ticket_detail'),
    path('new/', create_or_edit_ticket, name='new_ticket'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_ticket, name='edit_ticket'),
    url(r'^(?P<pk>\d+)/upvote/$', upvote, name='upvote_ticket')
]