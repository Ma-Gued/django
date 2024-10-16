import random
from django import template

register = template.Library()

@register.filter
def add_random_char(value, chars):
    if not value:
        return value
    random_char = random.choice(chars)
    return f"{value} {random_char}"