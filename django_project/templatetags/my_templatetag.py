from django import template

from .static_cache import build_cache_id

register = template.Library()


@register.filter(name='create_cache_id')
def create_cache_id(static_path: str) -> str:
    return build_cache_id(static_path)
