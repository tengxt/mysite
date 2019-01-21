from django.contrib import admin
from .models import ReadNum, ReadDetail, ImagesList

@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'content_object')

@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('date', 'read_num', 'content_object')

@admin.register(ImagesList)
class ImagesListAdmin(admin.ModelAdmin):
    list_display = ('pic',)
