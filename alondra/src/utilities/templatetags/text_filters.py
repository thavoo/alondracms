from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()
@register.filter
@stringfilter
def lower(value):
    return value.lower()
@register.filter
@stringfilter
def getfirstword(value):
    print value.split()

    return value.split()[1]

