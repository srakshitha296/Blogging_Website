from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def list_post(request):
    blog_posts = Post.objects.all()
    return render(request, 'home.html', {'blog_posts':blog_posts})

def view_post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'view_post.html', {'post':post})

def add_post(request):
    return render(request, 'add.html')

def edit_post(request):
    return render(request, 'edit.html')

def delete_post(request):
    return render(request, 'delete.html')

