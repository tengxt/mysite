from django.shortcuts import render, redirect
from read_statistics.utils import get_7_days_hot_blogs
from django.views.decorators.cache import cache_page
from blog.models import Blog
from visits.utils import change_info

@cache_page(60*10)          #缓存整个网页10分钟
def home(request):
    change_info(request)
    context = {}
    context['hot_blogs_for_7_days'] = get_7_days_hot_blogs()
    context['get_article_all'] = Blog.objects.order_by('-created_time')[:10]
    return render(request, 'home.html', context)

@cache_page(60*10)
def time(request):
    change_info(request)
    context = {}
    context['blogs'] = Blog.objects.all()[:10]
    return render(request, 'time.html', context)

@cache_page(60*10)
def share(request):
    change_info(request)
    context={}
    return render(request, 'share.html', context)

