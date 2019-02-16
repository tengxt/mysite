from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField(verbose_name='评论内容')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    user = models.ForeignKey(User, related_name="comments", verbose_name='评论用户', on_delete=models.CASCADE)

    root = models.ForeignKey('self', related_name='root_comment', verbose_name='文章根目录', null=True,
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='parent_comment', verbose_name='父级目录', null=True,
                               on_delete=models.CASCADE)
    reply_to = models.ForeignKey(User, related_name="replies", verbose_name='回复评论', null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.text

    def get_url(self):
        return self.content_object.get_url()

    def get_user(self):
        return self.user

    class Meta:
        ordering = ['comment_time']
        verbose_name = '评论列表'
        verbose_name_plural = verbose_name