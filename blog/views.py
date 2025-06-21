from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all().order_by("-date")
    context = {
        'posts':posts,
        'title':'Главная страница блога'

    }
    return render(request,'post_list.html',context)


def post_detail(request,pk):
    posts = get_object_or_404(Post,pk=pk)
    context = {
        'posts':posts,
        'title':posts.title

    }
    return render(request,'post_detail.html',context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request,'post_form.html',{'form':form})

@login_required
def edit_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'post_form.html',{'form':form})


def delete_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html', {'form':form})



