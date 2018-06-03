import requests
import json
from django.conf import settings
from django import template
from posts.models import PostItem
from utilities.paginator import paginator

register = template.Library()
@register.assignment_tag(name='get_related_videos', takes_context=True)
def get_related_videos(context,parent_id,limit=5):
    videos = []
    headers = {
        "User-Agent": "Gamajuegos Browser",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "application/json; charset=utf-8",
        "Accept-Language": "es-MX,es;q=0.8",
        "Connection": "keep-alive",
        'Content-type': 'application/json; charset=utf-8'
    }

    r = requests.post(
        settings.GET_VIDEO_RELATED_LIST, 
        data=json.dumps({'parent_id':parent_id,'limit':limit}), 
        headers=headers
    )
    r.encoding = 'utf-8'
    if r.status_code == 200:
       videos = json.loads(r.text.encode('utf-8')).get('items',[])
    return videos

@register.assignment_tag(name='get_recent_videos', takes_context=True)
def get_recent_videos(context,limit=5):
    videos = []
    
    headers = {
        "User-Agent": "Gamajuegos Browser",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "application/json; charset=utf-8",
        "Accept-Language": "es-MX,es;q=0.8",
        "Connection": "keep-alive",
        'Content-type': 'application/json; charset=utf-8'
    }

    r = requests.post(
        settings.VIDEOS_LIST, 
        data=json.dumps({'page':1,'limit':limit}), 
        headers=headers
    )
    r.encoding = 'utf-8'
    if r.status_code == 200:
        videos = json.loads(r.text.encode('utf-8'))
        videos = videos.get('items',[])
    return videos
