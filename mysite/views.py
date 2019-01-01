import datetime
from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from read_statistics.utils import get_seven_days_read_data, get_today_hot_data
from blog.models import Blog


def get_7_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects \
                .filter(read_details__date__lt=today, read_details__date__gte=date) \
                .values('id', 'title') \
                .annotate(read_num_sum=Sum('read_details__read_num')) \
                .order_by('-read_num_sum')
    print('blogs ====> %s', blogs)
    return blogs[:5]

def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)

    # 获取7天热门博客的缓存数据
    hot_blogs_for_7_days = cache.get('hot_blogs_for_7_days')
    if hot_blogs_for_7_days is None:
        hot_blogs_for_7_days = get_7_days_hot_blogs()
        cache.set('hot_blogs_for_7_days', hot_blogs_for_7_days, 3600)

    # 获取首页博客信息的缓存数据
    blogs = cache.get('blogs')
    if blogs is None:
        blogs = Blog.objects.all()[:10]
        cache.set('blogs', blogs, 3600)

    # 获取最热文章的缓存数据
    today_hot_data = cache.get('today_hot_data')
    if today_hot_data is None:
        today_hot_data = get_today_hot_data(blog_content_type)
        cache.set('today_hot_data', today_hot_data, 3600)

    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = today_hot_data
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

def comment(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    # 获取最热文章的缓存数据
    today_hot_data = cache.get('today_hot_data')
    if today_hot_data is None:
        today_hot_data = get_today_hot_data(blog_content_type)
        cache.set('today_hot_data', today_hot_data, 3600)

    context = {}
    context['today_hot_data'] = today_hot_data
    return render(request, 'comment.html', context)

