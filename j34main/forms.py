from django.forms import ModelForm
from django.db import models
from .models import Content

def urlfields_assume_https(db_field, **kwargs):
    """
    ModelForm.Meta.formfield_callback function to assume HTTPS for scheme-less
    domains in URLFields.
    This may not be needed starting with Django 6.0
    per https://adamj.eu/tech/2023/12/07/django-fix-urlfield-assume-scheme-warnings/ 
    """
    if isinstance(db_field, models.URLField):
        kwargs["assume_scheme"] = "https"
    return db_field.formfield(**kwargs)

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = [
            "title",
            "sub_title",
            "featured_image",
            "image_caption",
            "teaser",
            "content",
            "categories",
        ]
        formfield_callback = urlfields_assume_https
