import nh3

from django.forms import ModelForm
from django import forms
from django.db import models
from .models import Content, Category


class ContentForm(forms.Form):
    title = forms.CharField(label="Title")
    sub_title = forms.CharField(label="Subtitle")
    featured_image = forms.URLField(
        label="Featured Image", 
        assume_scheme="https", # remove argument for Django 6.0
        )
    image_caption = forms.CharField(label="Caption for Featured Image")
    teaser = forms.CharField(label="Teaser", widget=forms.Textarea())
    content = forms.CharField(label="Content of Blog", widget=forms.Textarea())
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        label="Categories"
        )
    

class HtmlSanitizedCharField(forms.CharField):
    def to_python(self, value):
        value = super().to_python(value)
        if value not in self.empty_values:
            value = nh3.clean(value)
        return value


class AdditionalContentHtmlForm(forms.Form):
    order = forms.IntegerField(label="Order")
    is_raw_html = forms.BooleanField(label="Is this raw HTML?")
    additional_content = HtmlSanitizedCharField(label="HTML Content", widget=forms.Textarea())


class AdditionalContentMarkdownForm(forms.Form):
    order = forms.IntegerField(label="Order")
    is_raw_html = forms.BooleanField(label="Is this raw HTML?")
    additional_content = forms.CharField(label="Markdown Content", widget=forms.Textarea())
