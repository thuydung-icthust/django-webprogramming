from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def register(request):
    """Register a new user. """
    if request.method != 'POST':
        # display a blank register form
        form = UserCreationForm()
    else:
        # Process updated form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('blogs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
