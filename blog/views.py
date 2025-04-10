from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    context = {
        'posts':posts,
        'title':'Главная страница блога'

    }
    return render(request,'blog/post_list.html',context)




