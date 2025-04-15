from django.shortcuts import render, get_object_or_404
from .models import Post


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




