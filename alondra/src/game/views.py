import requests 
import json
from django.db.models import Q
from django.conf import settings
from django.template.response import TemplateResponse
from django.utils import timezone
from utilities.paginator import paginator
from django.http import Http404

def games(request, slug=None, page=1, model=None):

    context = {}
    template_name = [
            'modules/games/games.html' ,
         
        ]
    return TemplateResponse(request, template_name, context)

def game(request, slug=None):
    
    context = {'gameinfo':None,'videos':[]}

    headers = {
        "User-Agent": "Gamajuegos Browser",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "application/json; charset=utf-8",
        "Accept-Language": "es-MX,es;q=0.8",
        "Connection": "keep-alive",
        'Content-type': 'application/json; charset=utf-8'
    }

    r = requests.post(
        settings.GET_GAME, 
        data = json.dumps({'slug':slug}), 
        headers=headers
    )
    r.encoding = 'utf-8'
    if r.status_code == 204:
        raise Http404
        
    if r.status_code < 400:
        try:
            context['gameinfo'] = json.loads(r.text.encode('utf-8'))
            headers = {
                "User-Agent": "Gamajuegos Browser",
                "Accept-Encoding": "gzip, deflate",
                "Accept": "application/json; charset=utf-8",
                "Accept-Language": "es-MX,es;q=0.8",
                "Connection": "keep-alive",
                'Content-type': 'application/json; charset=utf-8'
            }

            r = requests.post(
                settings.GET_VIDEO, 
                data = json.dumps({'parent_id':context['gameinfo'].get('id')}), 
                headers=headers
            )
            r.encoding = 'utf-8'
            
            if r.status_code < 400:
                context['videos'] = json.loads(r.text.encode('utf-8'))
                

            r = requests.post(
                settings.GET_VIDEO_PARENT_LIST, 
                data = json.dumps({'parent_id':context['gameinfo'].get('id')}), 
                headers=headers
            )
            r.encoding = 'utf-8'
            
            if r.status_code < 400:
                context['video_items'] = json.loads(r.text.encode('utf-8'))
                

        except ValueError :
            raise Http404
        
        
       
    else:
        raise Http404




    template_name =  [
            'modules/games/game.html',
          
        ] 
    return TemplateResponse(request, template_name, context)

