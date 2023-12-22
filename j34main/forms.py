import nh3

from django.forms import ModelForm
from django import forms
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


class HtmlSanitizedCharField(forms.CharField):
    def to_python(self, value):
        value = super().to_python(value)
        if value not in self.empty_values:
            value = nh3.clean(value)
        return value
    

class AdditionalContentHtmlForm(forms.Form):
    order = forms.IntegerField(label="Order")
    is_raw_html = forms.BooleanField(label="Is this raw HTML?")
    additional_content = HtmlSanitizedCharField(label="HTML Content")


class AdditionalContentMarkdownForm(forms.Form):
    order = forms.IntegerField(label="Order")
    is_raw_html = forms.BooleanField(label="Is this raw HTML?")
    additional_content = forms.CharField(label="Markdown Content")
