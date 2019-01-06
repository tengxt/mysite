from django.contrib import admin
from .models import BlogType, Blog, BlogTag

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

@admin.register(BlogTag)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_type', 'blog_tag', 'picture', 'author', 'get_read_num', 'created_time', 'last_updated_time')
