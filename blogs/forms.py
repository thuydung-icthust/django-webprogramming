from django import forms
from .models import BlogPost, Contact


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'text')
       # title = ['text']
        #content = ['text']
        labels = {'title': 'Title', 'text': 'Content', }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('fullname', 'email', 'title', 'text')
        labels = {'fullname': 'Full name', 'email': 'Email', 'title': 'Title', 'text': 'Your message',}
