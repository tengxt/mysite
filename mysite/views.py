from django.shortcuts import render
from read_statistics.utils import get_7_days_hot_blogs
from django.core.cache import cache
from blog.models import Blog
from visits.utils import change_info

def home(request):
    change_info(request)
    context = {}
    num = Blog.objects.all().count()
    context['hot_blogs_for_7_days'] = get_7_days_hot_blogs()
    blogs_key = 'blogs_key_{0}'.format(num)
    if cache.has_key(blogs_key):
        blogs_val = cache.get(blogs_key)
    else:
        blogs_val = Blog.objects.order_by('-last_updated_time')[:10]
        cache.set(blogs_key, blogs_val, 3600)
    context['get_article_all'] = blogs_val
    return render(request, 'home.html', context)




