from django.contrib.sitemaps import Sitemap
from .models import Tool


class ToolSitemap(Sitemap):

    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Tool.objects.all()

    def location(self, obj):
        return f"/tools/{obj.slug}/"
    
class ToolLandingSitemap(Sitemap):

    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Tool.objects.all()

    def location(self, obj):
        return f"/tool/{obj.slug}/online/"