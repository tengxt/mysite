from django.db import models
from django.utils import timezone

#访问网站的ip地址和次数
class Userip(models.Model):
    ip=models.CharField(verbose_name='IP地址',max_length=30)    #ip地址
    count=models.IntegerField(verbose_name='访问次数',default=0) #该ip访问次数
    class Meta:
        verbose_name = '访问用户信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.ip

#网站总访问次数
class VisitNumber(models.Model):
    count=models.IntegerField(verbose_name='网站访问总次数',default=0) #网站访问总次数
    class Meta:
        verbose_name = '网站访问总次数'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.count)

#单日访问量统计
class DayNumber(models.Model):
    day=models.DateField(verbose_name='日期',default=timezone.now)
    count=models.IntegerField(verbose_name='网站访问次数',default=0) #网站访问总次数
    class Meta:
        verbose_name = '网站日访问量统计'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.day)
