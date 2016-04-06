from django import template


register = template.Library()


@register.filter
def hash_html(value):
    from posts.utils import wrrap_link_node
    return wrrap_link_node(value)
