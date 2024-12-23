from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

def main_view(request):
    return render(request, "base.html")

def html_view(request):
    return render(request, "base.html")

def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/posts_list.html", context={"posts": posts})


def posts_detail_view(request, id):
    post = Post.objects.get(id=id)
    return render(request, "posts/posts_detail.html", context={"post": post})
