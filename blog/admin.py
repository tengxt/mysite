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

    class Media:
        css = {'all':(
            'blog/css/simditor.css',
            'blog/css/simditor-html.css',
            'blog/css/simditor-markdown.css',
        )}
        js = (
            'https://cdn.bootcss.com/jquery/3.2.1/jquery.js',
            'https://cdn.bootcss.com/js-beautify/1.7.5/beautify-html.js',
            'https://cdn.bootcss.com/marked/0.3.12/marked.js',
            'https://cdn.bootcss.com/to-markdown/3.1.1/to-markdown.js',
            'blog/js/simditor/module.js',
            'blog/js/simditor/uploader.js',
            'blog/js/simditor/hotkeys.js',
            'blog/js/simditor/simditor.js',
            'blog/js/simditor/simditor-autosave.js',
            'blog/js/simditor/simditor-html.js',
            'blog/js/simditor/simditor-markdown.js',
            'blog/js/textarea.js',
        )
