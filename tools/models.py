from django.db import models

class Tool(models.Model):

    name = models.CharField(max_length=100)

    slug = models.SlugField(unique=True)

    url = models.CharField(max_length=200)

    category = models.CharField(max_length=50)

    icon = models.CharField(max_length=10, blank=True)

    description = models.TextField(blank=True)

    seo_title = models.CharField(max_length=200, blank=True)

    seo_description = models.TextField(blank=True)

    usage_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name