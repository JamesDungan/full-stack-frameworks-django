from django.test import TestCase, Client, SimpleTestCase
from .models import Post
from django.contrib.auth.models import User
from pprint import pprint
from urllib.parse import urlencode

class BlogpostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', email='jdoe@gmail.com',password='1234')
        self.superuser = User.objects.create_superuser(username='test_author_1', email='jdoe@gmail.com',password='1234')
        Post.objects.create(title="test post 1", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut cursus massa. Sed odio est, interdum a dapibus sed, pretium vel ipsum. Etiam varius condimentum odio sodales posuere. Aenean viverra, velit nec dignissim porta, massa purus porta lorem, non pellentesque ipsum nulla et metus. Nullam aliquet ante vel ex pretium, vel aliquet ante consectetur. Etiam laoreet nisi porta tortor eleifend elementum. Donec sagittis ac nulla ullamcorper varius. Sed egestas sollicitudin nibh, sed convallis magna pharetra vitae. Aliquam ex diam, bibendum quis scelerisque a, consectetur sit amet lacus. Aliquam et magna vitae arcu dapibus consequat.",tag="test tag 1", author="test_author_1")
        Post.objects.create(title="test post 2", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut cursus massa. Sed odio est, interdum a dapibus sed, pretium vel ipsum. Etiam varius condimentum odio sodales posuere. Aenean viverra, velit nec dignissim porta, massa purus porta lorem, non pellentesque ipsum nulla et metus. Nullam aliquet ante vel ex pretium, vel aliquet ante consectetur. Etiam laoreet nisi porta tortor eleifend elementum. Donec sagittis ac nulla ullamcorper varius. Sed egestas sollicitudin nibh, sed convallis magna pharetra vitae. Aliquam ex diam, bibendum quis scelerisque a, consectetur sit amet lacus. Aliquam et magna vitae arcu dapibus consequat.",tag="test tag 2", author="test_author_2")
        Post.objects.create(title="test post 3", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut cursus massa. Sed odio est, interdum a dapibus sed, pretium vel ipsum. Etiam varius condimentum odio sodales posuere. Aenean viverra, velit nec dignissim porta, massa purus porta lorem, non pellentesque ipsum nulla et metus. Nullam aliquet ante vel ex pretium, vel aliquet ante consectetur. Etiam laoreet nisi porta tortor eleifend elementum. Donec sagittis ac nulla ullamcorper varius. Sed egestas sollicitudin nibh, sed convallis magna pharetra vitae. Aliquam ex diam, bibendum quis scelerisque a, consectetur sit amet lacus. Aliquam et magna vitae arcu dapibus consequat.",tag="test tag 3", author="test_author_3")
        Post.objects.create(title="test post 4", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut cursus massa. Sed odio est, interdum a dapibus sed, pretium vel ipsum. Etiam varius condimentum odio sodales posuere. Aenean viverra, velit nec dignissim porta, massa purus porta lorem, non pellentesque ipsum nulla et metus. Nullam aliquet ante vel ex pretium, vel aliquet ante consectetur. Etiam laoreet nisi porta tortor eleifend elementum. Donec sagittis ac nulla ullamcorper varius. Sed egestas sollicitudin nibh, sed convallis magna pharetra vitae. Aliquam ex diam, bibendum quis scelerisque a, consectetur sit amet lacus. Aliquam et magna vitae arcu dapibus consequat.",tag="test tag 4", author="test_author_4")

        self.client = Client()

    def test_get_posts(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get('/posts/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 4)
        self.assertTemplateUsed(response=response, template_name='blogposts.html')

    def test_post_detail(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get('/posts/1/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response=response, template_name='postdetail.html')
        self.assertEqual(response.context['post'].views, 1)

    def test_create_post_staff(self):
        self.client.login(username='test_author_1', password='1234')
        response = self.client.get('/posts/new/')

        self.assertEqual(response.status_code, 200)        
        self.assertTemplateUsed(response=response, template_name='blogpostform.html')

        data = urlencode({"title":"test", "content":"content", "tag":"tag"})
        response = self.client.post('/posts/new/', data, content_type="application/x-www-form-urlencoded", follow=True)
        self.assertContains(response, '<p><span class="boldtext">Author:</span>', status_code=200)

    def test_create_post_non_staff(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get('/posts/new/', follow=True)
        self.assertContains(response, '<h2 class="text-center">Tickets</h2>', status_code=200)

    def test_edit_post_staff(self):
        self.client.login(username='test_author_1', password='1234')
        response = self.client.get('/posts/1/edit/')
        self.assertEqual(response.status_code, 200)        
        self.assertTemplateUsed(response=response, template_name='blogpostform.html')
        data = urlencode({"title":"test", "content":"content", "tag":"tag"})
        response = self.client.post('/posts/1/edit/', data, content_type="application/x-www-form-urlencoded", follow=True)
        self.assertContains(response, '<p><span class="boldtext">Author:</span>', status_code=200)
    
    def test_edit_post_non_staff(self):
        self.client.login(username='user1', password='1234')
        response = self.client.get('/posts/1/edit/', follow=True)
        self.assertContains(response, '<h2 class="text-center">Tickets</h2>', status_code=200)
