from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

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

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request,'post_form.html',{'form':form})


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




