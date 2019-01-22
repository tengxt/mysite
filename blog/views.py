from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.core.cache import cache
from django.conf import settings
from django.db.models import Count
from read_statistics.utils import get_7_days_hot_blogs, pics_list
from .models import Blog, BlogType, BlogTag
from read_statistics.utils import read_statistics_once_read


def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get('page', 1) # 获取url的页面参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)
    currentr_page_num = page_of_blogs.number # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['hot_blogs_for_7_days'] = get_7_days_hot_blogs()
    context['background'] = pics_list()
    return context

# 获取日期归档对应的博客数量
def get_blog_dates_data():
    blog_dates = Blog.objects.dates('created_time', 'month', order="DESC")
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year,
                                         created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count
    return blog_dates_dict

def blog_list(request):
    blogs_all_list = Blog.objects.filter(blog_style='文章')
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))
    context['blog_tags'] = BlogTag.objects.annotate(blog_count=Count('blog'))
    context['blog_dates'] = get_blog_dates_data()
    return render(request, 'blog/blog_list.html', context)

def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request, blogs_all_list)

    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))
    context['blog_tags'] = BlogTag.objects.annotate(blog_count=Count('blog'))
    context['blog_dates'] = get_blog_dates_data()
    return render(request, 'blog/blogs_with_type.html', context)

def blogs_with_tag(request, blog_tag_pk):
    blog_tag = get_object_or_404(BlogTag, pk=blog_tag_pk)
    hot_tags_key = 'hot_tags_key'
    if cache.has_key(hot_tags_key):
        hot_tags_val = cache.get(hot_tags_key)
    else:
        hot_tags_val = Blog.objects.filter(blog_tag=blog_tag)
        cache.set(hot_tags_val, hot_tags_val, 3600)
    context = get_blog_list_common_data(request, hot_tags_val)

    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))
    context['blog_tags'] = BlogTag.objects.annotate(blog_count=Count('blog'))
    context['blog_dates'] = get_blog_dates_data()
    return render(request, 'blog/blogs_with_tag.html', context)

def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = '%s年%s月' % (year, month)

    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))
    context['blog_tags'] = BlogTag.objects.annotate(blog_count=Count('blog'))
    context['blog_dates'] = get_blog_dates_data()
    return render(request, 'blog/blogs_with_date.html', context)

def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    read_cookie_key = read_statistics_once_read(request, blog)
    context = {}
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['blog'] = blog
    context['blog_tags'] = BlogTag.objects.annotate(blog_count=Count('blog'))
    context['hot_blogs_for_7_days'] = get_7_days_hot_blogs()
    context['background'] = pics_list()
    response = render(request, 'blog/blog_detail.html', context) # 响应
    response.set_cookie(read_cookie_key, 'true') # 阅读cookie标记
    return response

# 资源分享页
def blog_share(request):
    share_list = Blog.objects.filter(blog_style='资源')
    context = get_blog_list_common_data(request, share_list)
    return render(request, 'blog/blog_share.html', context)

# 时间轴页
def blog_timer(request):
    timer_list = Blog.objects.all().order_by('-created_time')
    context = get_blog_list_common_data(request, timer_list)
    return render(request, 'blog/blog_timer.html', context)