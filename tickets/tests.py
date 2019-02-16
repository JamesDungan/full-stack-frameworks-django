from django.test import TestCase, Client
from tickets.models import Ticket
from django.contrib.auth.models import User
from urllib.parse import urlencode

class TicketsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', email='jdoe@gmail.com',password='1234')
        self.superuser = User.objects.create_superuser(username='test_author_1', email='jdoe@gmail.com',password='1234')
        Ticket.objects.create(title="test ticket 1", text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut cursus massa. Sed odio est, interdum a dapibus sed, pretium vel ipsum. Etiam varius condimentum odio sodales posuere. Aenean viverra, velit nec dignissim porta, massa purus porta lorem, non pellentesque ipsum nulla et metus. Nullam aliquet ante vel ex pretium, vel aliquet ante consectetur. Etiam laoreet nisi porta tortor eleifend elementum. Donec sagittis ac nulla ullamcorper varius. Sed egestas sollicitudin nibh, sed convallis magna pharetra vitae. Aliquam ex diam, bibendum quis scelerisque a, consectetur sit amet lacus. Aliquam et magna vitae arcu dapibus consequat.",ticket_type="Feature", created_by="user1")
        Ticket.objects.create(title="test ticket 2", text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut cursus massa. Sed odio est, interdum a dapibus sed, pretium vel ipsum. Etiam varius condimentum odio sodales posuere. Aenean viverra, velit nec dignissim porta, massa purus porta lorem, non pellentesque ipsum nulla et metus. Nullam aliquet ante vel ex pretium, vel aliquet ante consectetur. Etiam laoreet nisi porta tortor eleifend elementum. Donec sagittis ac nulla ullamcorper varius. Sed egestas sollicitudin nibh, sed convallis magna pharetra vitae. Aliquam ex diam, bibendum quis scelerisque a, consectetur sit amet lacus. Aliquam et magna vitae arcu dapibus consequat.",ticket_type="Feature", created_by="test_author_2")
        Ticket.objects.create(title="test ticket 3", text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut cursus massa. Sed odio est, interdum a dapibus sed, pretium vel ipsum. Etiam varius condimentum odio sodales posuere. Aenean viverra, velit nec dignissim porta, massa purus porta lorem, non pellentesque ipsum nulla et metus. Nullam aliquet ante vel ex pretium, vel aliquet ante consectetur. Etiam laoreet nisi porta tortor eleifend elementum. Donec sagittis ac nulla ullamcorper varius. Sed egestas sollicitudin nibh, sed convallis magna pharetra vitae. Aliquam ex diam, bibendum quis scelerisque a, consectetur sit amet lacus. Aliquam et magna vitae arcu dapibus consequat.",ticket_type="Feature", created_by="test_author_3")
        Ticket.objects.create(title="test ticket 4", text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut cursus massa. Sed odio est, interdum a dapibus sed, pretium vel ipsum. Etiam varius condimentum odio sodales posuere. Aenean viverra, velit nec dignissim porta, massa purus porta lorem, non pellentesque ipsum nulla et metus. Nullam aliquet ante vel ex pretium, vel aliquet ante consectetur. Etiam laoreet nisi porta tortor eleifend elementum. Donec sagittis ac nulla ullamcorper varius. Sed egestas sollicitudin nibh, sed convallis magna pharetra vitae. Aliquam ex diam, bibendum quis scelerisque a, consectetur sit amet lacus. Aliquam et magna vitae arcu dapibus consequat.",ticket_type="Feature", created_by="test_author_4")

        self.client = Client()

    def test_get_tickets(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get('/tickets/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['tickets']), 4)
        self.assertTemplateUsed(response=response, template_name='tickets.html')

    def test_ticket_detail(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get('/tickets/1/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response=response, template_name='ticketdetail.html')
    
    def comment_on_ticket(self):
        self.client.login(username='user1', password='1234')
        data = urlencode({"text":"Test Comment"})
        response = self.client.post('/tickets/1/', data, content_type="application/x-www-form-urlencoded", follow=True)
        self.assertEqual(response.status_code, 200)        
        self.assertTemplateUsed(response=response, template_name='ticketdetail.html')

    def test_create_ticket(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get('/tickets/new/')

        self.assertEqual(response.status_code, 200)        
        self.assertTemplateUsed(response=response, template_name='ticketform.html')

        data = urlencode({"title":"test", "text":"content", "ticket_type":"Feature"})
        response = self.client.post('/tickets/new/', data, content_type="application/x-www-form-urlencoded", follow=True)
        self.assertContains(response, '<p class="ticket-footer-label">Type:</p>', status_code=200)

    def test_owner_edits_ticket(self):
        self.client.login(username='user1', password='1234')
        data = urlencode({"title":"test", "text":"content", "ticket_type":"Feature"})
        response = self.client.post('/tickets/1/edit/', data, content_type="application/x-www-form-urlencoded", follow=True)
        self.assertContains(response, '<p class="ticket-footer-label">Type:</p>', status_code=200)
    
    def test_non_owner_edits_ticket(self):
        self.client.login(username='test_author_1', password='1234')
        data = urlencode({"title":"test", "text":"content", "ticket_type":"Feature"})
        response = self.client.post('/tickets/1/edit/', data, content_type="application/x-www-form-urlencoded", follow=True)
        self.assertContains(response, '<p class="ticket-footer-label">Type:</p>', status_code=200)

