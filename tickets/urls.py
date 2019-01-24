from django.urls import path, include
from django.conf.urls import url
from .views import all_tickets, ticket_detail

urlpatterns = [
    path('', all_tickets, name='tickets'),
    url(r'^(?P<pk>\d+)/$', ticket_detail, name='ticket_detail'),
]