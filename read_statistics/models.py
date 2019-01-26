from django.db import models
from django.db.models.fields import exceptions
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

class ReadNum(models.Model):
    read_num = models.IntegerField(verbose_name='阅读量', default=0)

    content_type = models.ForeignKey(ContentType, verbose_name='文章类型', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = '文章的累计阅读量'
        verbose_name_plural = verbose_name

class ReadNumExpandMethod():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0

class ReadDetail(models.Model):
    date = models.DateField(verbose_name='时间', default=timezone.now)
    read_num = models.IntegerField(verbose_name='阅读量', default=0)

    content_type = models.ForeignKey(ContentType, verbose_name='文章类型', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = '文章的每日阅读量'
        verbose_name_plural = verbose_name

class ImagesList(models.Model):
    pic = models.CharField(verbose_name='图片地址', max_length=200)

    class Meta:
        verbose_name = '背景图片详情列表'
        verbose_name_plural = verbose_name

class LinksList(models.Model):
    link_name = models.CharField(verbose_name='友链名称', max_length=100)
    link_href = models.CharField(verbose_name='友链地址', max_length=200)
    link_pic = models.CharField(verbose_name='友链图标地址', max_length=200, blank=True)
    link_content = models.TextField(verbose_name='友链的描述', blank=True)
