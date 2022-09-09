from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    form = BlogForm()
    context = {
        'blogs' : blogs,
        'form' : form
    }
    return render(request, 'blog/home.html', context)

def blog_create(request):
    form = BlogForm()
    if request.method =='POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {
        'form':form
    }

    return render(request, 'blog/blog_add.html', context)


def blog_update(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(instance=blog)

    if request.method =='POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')

    

    context = {
        "blog" : blog,
        "form" : form
    }

    return render(request, 'blog/blog_update.html', context)

def blog_delete(request, id):
    blog = Blog.objects.get(id=id)

    if request.method =='POST':
        blog.delete()
        return redirect('home')

    context = {
        'blog' : blog
    }

    return render(request, 'blog/blog_delete.html', context)
