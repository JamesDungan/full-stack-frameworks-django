from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Postfields = ('title', 'content', 'image', 'tag', 'published_date')