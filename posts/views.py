from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post
from django.db.models import Q
from posts.forms import PostForm, SearchForm
from django.contrib.auth.decorators import login_required





def main_view(request):
    if request.method == "GET":
        return render(request, "base.html")


def html_view(request):
    return render(request, "base.html")


@login_required(login_url="login-view")
def posts_list_view(request):
    if request.method == "GET":
        limit = 2 
        page = int(request.GET.get("page", 1))
        search=request.GET.get("search")
        category = request.GET.get("category")
        ordering = request.GET.get("ordering")
        form = SearchForm(request.GET) 
        posts = Post.objects.all()
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(description__icontaifns=search))

        if category:
            posts= posts.filter(category_id=category)
        if ordering:
              posts = posts.order_by(ordering)
        max_pages = posts.count() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)
        start = (page - 1) * limit
        end = page * limit
        posts = posts[start:end]
        return render(request, "posts/posts_list.html", context={"posts": posts, 
                                                                 "form" : form, 'max_pages': range(1, max_pages + 1)})


@login_required(login_url="login-view")
def posts_detail_view(request, id):
    if request.method == "GET": 
        post = Post.objects.get(id=id)
        return render(request, "posts/posts_detail.html", context={"post": post})


@login_required(login_url="login-view")
def create_post_view(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "posts/posts_create.html", context={"form": form})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form": form})
        elif form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]
            post = Post.objects.create(title=title, description=description, image=image)
            return redirect("/posts/")
