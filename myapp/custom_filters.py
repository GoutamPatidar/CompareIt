from django import template

register = template.Library()

@register.filter
def get_item(value, index):
    return value[index]
