from django.contrib.sitemaps import Sitemap
from django.contrib.syndication.views import Feed
from blog.models import Blog

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.last_updated_time

    def location(self, obj):
        return "/blog/%s.html" % obj.id

class AllPostsRssFeed(Feed):
    title = "小涛个人博客"
    link = "/"
    description = "小涛博客，是一个记录技术心得和资源分享，记录生活点滴，分享兴趣爱好的个人博客。"

    def items(self):
        return Blog.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.blog_type, item.title)

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return "/blog/%s.html" % item.id
