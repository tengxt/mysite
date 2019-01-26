from django.contrib import admin
from .models import ReadNum, ReadDetail, ImagesList, LinksList

@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('id', 'read_num', 'content_object')

@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'read_num', 'content_object')

@admin.register(ImagesList)
class ImagesListAdmin(admin.ModelAdmin):
    list_display = ('id', 'pic')

@admin.register(LinksList)
class LinksListAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_name', 'link_href', 'link_pic', 'link_content')