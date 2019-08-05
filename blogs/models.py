from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        """ Return the text representation of the blog . """
        return self.title.upper()
        return self.text

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    text = models.TextField()

