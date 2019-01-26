import datetime
import random
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from blog.models import Blog
from .models import ReadNum, ReadDetail, ImagesList, LinksList


def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)

    if not request.COOKIES.get(key):
        # 总阅读数 +1
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()

        # 当天阅读数 +1
        date = timezone.now().date()
        readDetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        readDetail.read_num += 1
        readDetail.save()
    return key

def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums


# 7天内热门博客缓存
def get_7_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    hot_blogs_key = 'hot_blogs_key'
    if cache.has_key(hot_blogs_key):
        hot_blogs_val = cache.get(hot_blogs_key)
    else:
        hot_blogs_val = Blog.objects \
            .filter(read_details__date__lt=today, read_details__date__gte=date) \
            .values('id', 'title') \
            .annotate(read_num_sum=Sum('read_details__read_num')) \
            .order_by('-read_num_sum')[:5]
        cache.set(hot_blogs_key, hot_blogs_val, 3600)
    return hot_blogs_val

# background random
def pics_list():
    # 获取图片总数作为随机数
    num = ImagesList.objects.all().count()
    pics_key = 'pics_key_{0}'.format(num)
    if cache.has_key(pics_key):
        pics_val = cache.get(pics_key)
    else:
        pics_val = ImagesList.objects.all()
        cache.set(pics_key, pics_val, 3600)
    random_num = random.randint(1, num)
    pic_dict = {}
    for item in pics_val:
        pic_dict[item.id] = item.pic
    pic_dict_random = pic_dict.get(random_num)[6:]
    return pic_dict_random

def links_list():
    num = LinksList.objects.all().count()
    links_key = 'links_key_{0}'.format(num)
    if cache.has_key(links_key):
        links_val = cache.get(links_key)
    else:
        links_val = LinksList.objects.all()
        cache.set(links_key, links_val, 3600)
    return links_val
