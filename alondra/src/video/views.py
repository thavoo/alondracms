import requests 
import json
from django.db.models import Q
from django.conf import settings
from django.template.response import TemplateResponse
from django.utils import timezone
from utilities.paginator import paginator
from django.http import Http404

def videos(request, slug=None, page=1, model=None):

    next_page = 0
    prev_page = 0
    context = {'videos':[],'pages':1,'page':int(page),'next_page':next_page,'prev_page':prev_page}

    
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
        data=json.dumps({'page':page,'limit':10}), 
        headers=headers
    )
    r.encoding = 'utf-8'
    if r.status_code > 400:
        raise Http404
    if r.status_code == 200:
        videos = json.loads(r.text.encode('utf-8'))
        context['videos'] = videos.get('items',[])
        context['pages'] = videos.get('pages')+1
        if(page==1):
            context['next_page'] = int(page) +1
        if context['next_page'] < (context['pages']):
            context['next_page'] = int(page) +1
            if context['next_page'] >= (context['pages']):
                context['next_page'] = context['pages'] 
        if(page>1):
            context['prev_page'] = int(page) -1
            


    template_name = [
            'modules/videos/videos.html' ,
         
        ]
    return TemplateResponse(request, template_name, context)

def video(request, slug=None):
    
    context = {'video':None,'videos':[]}

    headers = {
        "User-Agent": "Gamajuegos Browser",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "application/json; charset=utf-8",
        "Accept-Language": "es-MX,es;q=0.8",
        "Connection": "keep-alive",
        'Content-type': 'application/json; charset=utf-8'
    }

    
    r = requests.post(
        settings.GET_VIDEO_DETAILS, 
        data = json.dumps({'slug':slug}), 
        headers=headers
    )
    r.encoding = 'utf-8'
    
    if r.status_code == 204:
        raise Http404
        
    if r.status_code < 400:
        try:
            context['video'] = json.loads(r.text.encode('utf-8'))
            

        except ValueError :
            raise Http404
        
        
       
    else:
        raise Http404




    template_name =  [
            'modules/videos/video.html',
        ] 
    return TemplateResponse(request, template_name, context)

