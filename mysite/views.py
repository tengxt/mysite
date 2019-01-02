from django.shortcuts import render, redirect
from read_statistics.utils import get_7_days_hot_blogs
from django.core.cache import cache
from blog.models import Blog


def home(request):
    # 获取首页博客信息的缓存数据
    blogs = cache.get('blogs')
    if blogs is None:
        blogs = Blog.objects.all()[:10]
        cache.set('blogs', blogs, 3600)

    context = {}
    context['hot_blogs_for_7_days'] = get_7_days_hot_blogs()
    context['get_article_all'] = blogs
    return render(request, 'home.html', context)

def time(request):
    # 获取首页博客信息的缓存数据
    blogs = cache.get('blogs')
    if blogs is None:
        blogs = Blog.objects.all()[:10]
        cache.set('blogs', blogs, 3600)

    context = {}
    context['blogs'] = blogs
    return render(request, 'time.html', context)

