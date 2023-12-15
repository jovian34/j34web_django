from django.contrib import admin

from .models import Content, Category, AdditionalContent

admin.site.register(Content)
admin.site.register(Category)
admin.site.register(AdditionalContent)
