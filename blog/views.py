from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request, 'blog/home.html', context)

def blog_create(request):
    form = BlogForm()

    context = {
        'form':form
    }

    return render(request, 'blog/blog_add.html', context)
