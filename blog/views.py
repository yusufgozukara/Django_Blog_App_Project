from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request, 'blog/home.html', context)
