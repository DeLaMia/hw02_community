from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.contrib.auth.decorators import login_required

LAST_10_POSTS: int = 10

@login_required
def index(request):
    posts = Post.objects.all()[:LAST_10_POSTS]
    context = {
        'posts': posts,
    }
    #    print(Post.objects.filter(pub_date__range=(start_date,end_date)).filter(text__contains=keyword).query) qfwqfqf
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:LAST_10_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
