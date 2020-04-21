from django.template import Library

register = Library()


@register.filter
def mod(value, value2):
    return value % value2
