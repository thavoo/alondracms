import requests 
import json
from django.db.models import Q
from django.conf import settings
from django.template.response import TemplateResponse
from django.utils import timezone
from django.http import Http404
from email_suscription.forms import EmailForm

def suscribe_to_serivice(request, slug=None):
    EmailForm
    context = {'Sucess':False,'videos':[]}

    headers = {
        "User-Agent": "Gamajuegos Browser",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "application/json; charset=utf-8",
        "Accept-Language": "es-MX,es;q=0.8",
        "Connection": "keep-alive",
        'Content-type': 'application/json; charset=utf-8'
    }

    
    r = requests.post(
        settings.GET_EMAIL_SUSCRIPTION_SERVICE_URL_DETAILS, 
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

