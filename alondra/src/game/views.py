import requests 
import json
from django.db.models import Q
from django.conf import settings
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils import timezone
from utilities.paginator import paginator
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from utilities.network import get_client_ip
from game.forms import RateForm

def games(request, slug=None, page=1, model=None):
    next_page = 0
    prev_page = 0
    context = {'games':[],'pages':1,'page':int(page),'next_page':next_page,'prev_page':prev_page}

    
    headers = {
        "User-Agent": "Gamajuegos Browser",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "application/json; charset=utf-8",
        "Accept-Language": "es-MX,es;q=0.8",
        "Connection": "keep-alive",
        'Content-type': 'application/json; charset=utf-8'
    }

    r = requests.post(
        settings.GAMES_LIST, 
        data=json.dumps({'page':page,'limit':10}), 
        headers=headers
    )
    r.encoding = 'utf-8'
    if r.status_code > 400:
        raise Http404
    if r.status_code == 200:
        games = json.loads(r.text.encode('utf-8'))
        context['games'] = games.get('items',[])
        context['pages'] = games.get('pages')+1
        if(page==1):
            context['next_page'] = int(page) +1
        if context['next_page'] < (context['pages']):
            context['next_page'] = int(page) +1
            if context['next_page'] >= (context['pages']):
                context['next_page'] = context['pages'] 
        if(page>1):
            context['prev_page'] = int(page) -1
            


    template_name = [
            'modules/games/games.html' ,
         
        ]
    return TemplateResponse(request, template_name, context)

def game(request, slug=None):
    
    context = {'gameinfo':None,'slug':slug,'videos':[],'images':[]}

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
                
            headers = {
                "User-Agent": "Gamajuegos Browser",
                "Accept-Encoding": "gzip, deflate",
                "Accept": "application/json; charset=utf-8",
                "Accept-Language": "es-MX,es;q=0.8",
                "Connection": "keep-alive",
                'Content-type': 'application/json; charset=utf-8'
            }

            r = requests.post(
                settings.GET_IMAGES_RELATED_LIST, 
                data=json.dumps({'parent_id':context['gameinfo'].get('id')}), 
                headers=headers
            )
            r.encoding = 'utf-8'
            if r.status_code == 200:
               context['images'] = json.loads(r.text.encode('utf-8'))





        except ValueError :
            raise Http404
        
        
       
    else:
        raise Http404



    template_name =  [
            'modules/games/game.html',
          
        ] 
    return TemplateResponse(request, template_name, context)


def rate_game(request, slug=None):
    gameinfo = None
    context2 = {'success':False}
    if request.method == "POST":
        x = request.POST
        form = RateForm(data=x)
        
        if form.is_valid():
            rating = form.cleaned_data.get('rating')
            ip = get_client_ip(request)
            
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
                data=json.dumps({'slug':slug}), 
                headers=headers
            )
            r.encoding = 'utf-8'
            if r.status_code == 204:
                raise Http404
                
            if r.status_code < 400:
                try:
                    gameinfo = json.loads(r.text.encode('utf-8'))  
                    headers = {
                        "User-Agent": "Gamajuegos Browser",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept": "application/json; charset=utf-8",
                        "Accept-Language": "es-MX,es;q=0.8",
                        "Connection": "keep-alive",
                        'Content-type': 'application/json; charset=utf-8'
                    }
                    
                    r = requests.post(
                        settings.GAMES_RATE, 
                        data=json.dumps({
                            'parent_id': int(gameinfo.get('id')),
                            'ip': ip,
                            'ratting': rating
                        }), 
                        headers=headers
                    )
                    r.encoding = 'utf-8'
                    if r.status_code == 200:
                        context2['success'] = True
                    if r.status_code > 400:
                        context2['success'] = False
                except ValueError :
                    raise Http404
            else:
                raise Http404

    return HttpResponse(json.dumps(context2))



def game_rating(request, slug=None):
    
    context = {'avg':None}
    if request.method == "POST":

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
            data=json.dumps({'slug':slug}), 
            headers=headers
        )
        r.encoding = 'utf-8'
        if r.status_code == 204:
            raise Http404
            
        if r.status_code < 400:
            try:
                gameinfo = json.loads(r.text.encode('utf-8'))  
                headers = {
                    "User-Agent": "Gamajuegos Browser",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept": "application/json; charset=utf-8",
                    "Accept-Language": "es-MX,es;q=0.8",
                    "Connection": "keep-alive",
                    'Content-type': 'application/json; charset=utf-8'
                }

                r = requests.post(
                    settings.GAMES_RATTING_AVG, 
                    data=json.dumps({'parent_id':gameinfo.get('id')}), 
                    headers=headers
                )
                r.encoding = 'utf-8'
                if r.status_code == 200:
                    avg = json.loads(r.text.encode('utf-8')).get('avg',None)
                    if avg is not None:
                        context['avg'] = avg.get('ratting__avg')

                   
            except ValueError :
                raise Http404
        else:
            raise Http404
    else:
        raise Http404

    return HttpResponse(json.dumps(context))