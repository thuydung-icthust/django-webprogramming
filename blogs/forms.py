from django import forms
from .models import BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'text')
       # title = ['text']
        #content = ['text']
        labels = {'title': 'Title', 'text': 'Content', }
