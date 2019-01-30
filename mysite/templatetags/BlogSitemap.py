from blog.models import Blog
from django.contrib.sitemaps import Sitemap

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.last_updated_time

    def location(self, obj):
        return "/blog/%s.html" % obj.id