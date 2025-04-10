from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by("-date")
    context = {
        'posts':posts,
        'title':'Главная страница блога'

    }
    return render(request,'post_list.html',context)




