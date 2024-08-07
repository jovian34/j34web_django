from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.db.models.functions import Now


class TrafficCounter(models.Model):
    page = models.CharField(null=False, max_length=128)
    timestamp = models.DateTimeField(db_default=Now())
    ip = models.CharField(null=True, max_length=64)
    user_agent = models.CharField(null=True, max_length=256)

    def __str__(self) -> str:
        return f"{self.timestamp}"


class Category(models.Model):
    cat_name = models.CharField(
        null=False,
        max_length=100,
    )

    def __str__(self) -> str:
        return self.cat_name


class Content(models.Model):
    title = models.CharField(
        null=False,
        max_length=100,
    )
    sub_title = models.CharField(db_default="", blank=True, max_length=100)
    author = models.CharField(db_default="Carl James", max_length=100)
    location = models.CharField(db_default="BLOOMINGTON, IN", max_length=100)
    pub_date = models.DateTimeField("date published", db_default=Now())
    featured_image = models.URLField(blank=True, null=True, max_length=200)
    image_caption = models.CharField(db_default="", blank=True, max_length=100)
    teaser = models.TextField(null=False)
    content = models.TextField(null=False)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class AdditionalContent(models.Model):
    main_content = models.ForeignKey(Content, null=False, on_delete=models.CASCADE)
    order = models.IntegerField(null=False)
    is_raw_html = models.BooleanField(db_default=False)
    additional_content = models.TextField(null=False)

    def __str__(self) -> str:
        return f"{self.main_content.title} part: {self.order}"
