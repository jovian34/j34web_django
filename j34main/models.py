from django.db import models


class Service(models.Model):
    service_name = models.CharField(null=False, max_length=100,)
    flat_rate = models.BooleanField(default=False)
    price = models.FloatField(default=40.0, blank=True, null=True)

    def __str__(self):
        return self.service_name


class Content(models.Model):
    title = models.CharField(null=False, max_length=100,)
    sub_title = models.CharField(default=None, blank=True, max_length=100)
    author = models.CharField(default='Carl James', max_length=100)
    location = models.CharField(default='BLOOMINGTON, IN', max_length=100)
    pub_date = models.DateTimeField('date published')
    featured_image = models.URLField(blank=True, null=True, max_length=200)
    teaser = models.TextField(null=False)
    content = models.TextField(null=False)

    def __str__(self):
        return self.title
