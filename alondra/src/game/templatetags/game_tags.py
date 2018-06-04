import requests
import json
from django.conf import settings
from django import template
from posts.models import PostItem
from utilities.paginator import paginator

register = template.Library()


@register.filter
def get_status(item):
    status = {
        'developemt':'En Desarrollo',
        'published':'Publicado',
        'unpublished':'Abandonado',
        'beta':'Fase Beta',
        'alpha':'Fase Alpha',
    }
    return status.get(item,'')

