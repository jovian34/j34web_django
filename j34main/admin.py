from django.contrib import admin

from .models import Content, Category, AdditionalContent, TrafficCounter

admin.site.register(Content)
admin.site.register(Category)
admin.site.register(AdditionalContent)

@admin.register(TrafficCounter)
class TrafficCounterAdmin(admin.ModelAdmin):
    model = TrafficCounter
    list_display = (
        "page",
        "timestamp",
        "ip",
        "user_agent",
    )
