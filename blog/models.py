from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from read_statistics.models import ReadNumExpandMethod, ReadDetail

class BlogType(models.Model):
    type_name = models.CharField(verbose_name='文章类型名称', max_length=15)

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name

class BlogTag(models.Model):
    tag_name = models.CharField(verbose_name='文章标签', max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name

class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(verbose_name='文章标题', max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    blog_tag = models.ForeignKey(BlogTag, on_delete=models.CASCADE)
    picture = models.CharField(verbose_name='文章缩略图', max_length=500)
    content = RichTextUploadingField(verbose_name='文章内容')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_updated_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    def get_url(self):
        return reverse('blog_detail', kwargs={'blog_pk': self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = '文章列表'
        verbose_name_plural = verbose_name
