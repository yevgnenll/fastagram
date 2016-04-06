from fastagram.utils import shrink_text

from django import template


register = template.Library()


@register.filter
def shrink_content(value):
    from fastagram.utils import shrink_text
    return shrink_text(value)
