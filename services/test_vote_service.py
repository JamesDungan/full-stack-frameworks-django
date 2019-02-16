from django.test import TestCase
from django.test.client import RequestFactory
from . import vote_service
from tickets.models import Ticket
from django.contrib.auth.models import User


class VoteServiceTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='user1', email='jdoe@gmail.com',password='1234')
        Ticket.objects.create(title="test ticket 1", text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut cursus massa. Sed odio est, interdum a dapibus sed, pretium vel ipsum. Etiam varius condimentum odio sodales posuere. Aenean viverra, velit nec dignissim porta, massa purus porta lorem, non pellentesque ipsum nulla et metus. Nullam aliquet ante vel ex pretium, vel aliquet ante consectetur. Etiam laoreet nisi porta tortor eleifend elementum. Donec sagittis ac nulla ullamcorper varius. Sed egestas sollicitudin nibh, sed convallis magna pharetra vitae. Aliquam ex diam, bibendum quis scelerisque a, consectetur sit amet lacus. Aliquam et magna vitae arcu dapibus consequat.",ticket_type="Feature", created_by="user1")


    def test_vote(self):
        request = self.factory.get('/tickets/')
        request.user = self.user
        request.session = {}
        request.session['ticket'] = 1

        ticket = vote_service.vote(request)

        self.assertEqual(ticket.votes, 1)

