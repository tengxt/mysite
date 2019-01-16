from django.shortcuts import render, redirect
from read_statistics.utils import get_7_days_hot_blogs
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from blog.models import Blog
from visits.utils import change_info

def home(request):
    change_info(request)
    context = {}
    context['hot_blogs_for_7_days'] = get_7_days_hot_blogs()
    blogs_key = 'blogs_key'
    if cache.has_key(blogs_key):
        blogs_val = cache.get(blogs_key)
    else:
        blogs_val = Blog.objects.order_by('-created_time')[:7]
        cache.set(blogs_key, blogs_val, 3600)
    context['get_article_all'] = blogs_val
    return render(request, 'home.html', context)

#@cache_page(60*15)
def time(request):
    change_info(request)
    context = {}
    context['blogs'] = Blog.objects.all()[:10]
    return render(request, 'time.html', context)

#@cache_page(60*15)
def share(request):
    change_info(request)
    context={}
    return render(request, 'share.html', context)

