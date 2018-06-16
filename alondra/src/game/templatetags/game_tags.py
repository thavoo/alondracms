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


@register.assignment_tag(name='get_top_games_users', takes_context=True)
def get_top_games_users(context):
    games = []

    headers = {
        "User-Agent": "Gamajuegos Browser",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "application/json; charset=utf-8",
        "Accept-Language": "es-MX,es;q=0.8",
        "Connection": "keep-alive",
        'Content-type': 'application/json; charset=utf-8'
    }
    
    r = requests.post(
        settings.GET_TOP_GAME_USERS_LIST,
        data=json.dumps({'page':1,'limit':7}), 
        headers=headers
    )
    r.encoding = 'utf-8'
    if r.status_code == 200:
    	games = json.loads(r.text.encode('utf-8')).get('items')  
	return games

