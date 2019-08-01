from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
#from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
# from .forms import BlogForm

# Create your views here.


def index(request):
    return render(request, 'blogs/index.html')


def blogposts(request):
    """ Show all blogs. """
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogposts.html', context)


def blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = BlogForm()
    else:
        # POST data submitted, process data.
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog=form.save(commit=False)
            new_blog.owner=request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('blogs:blogposts'))
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def edit_blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    if blog.owner == request.user:
        if request.method != 'POST':
            form = BlogForm(instance=blog)
        else:
            form = BlogForm(instance=blog, data=request.POST)
        #if blog.owner == request.user:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('blogs:blog',
                                                args=[blog.id]))
    else:
        return HttpResponseRedirect(reverse('blogs:blogposts'))    
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)
