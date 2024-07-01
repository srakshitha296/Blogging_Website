from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import blogForm

def list_post(request):
    blog_posts = Post.objects.all()
    return render(request, 'home.html', {'blog_posts':blog_posts})

def view_post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'view_post.html', {'post':post})

def add_post(request):
    if request.method == 'POST':
        form = blogForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('view_post', pk=post.pk)
    else:
        form = blogForm()
    return render(request, 'add_post.html', {'form': form})

def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = blogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            print("Post updated successfully")
            return redirect('view_post', pk=post.pk)
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = blogForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})


def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'GET':
        post.delete()
        return redirect('list_post')
    return render(request, 'delete_post.html', {'post': post})



