from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    if hasattr(dictionary, 'get'):
        return dictionary.get(key, 0)  # Return 0 instead of empty string for numbers
    return 0  # Default return for non-dict objects

@register.filter
def subtract(value, arg):
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def underscore_to_space(value):
    if value:
        return str(value).replace('_', ' ')
    return value