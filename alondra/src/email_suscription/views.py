import requests 
import json
from django.conf import settings
from django.http import HttpResponse
from email_suscription.forms import EmailForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def suscribe_to_serivice(request, slug=None):
    
    context = {'success':False}
    if request.method == "POST":
        x = request.POST
        form = EmailForm(
                data=x,
            )
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
    

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
                data = json.dumps({
                    'email': email,
                    'website':'www.gamajuegos.com'
                }), 
                headers=headers
            )
            r.encoding = 'utf-8'
            #print r.status_code
            #print r.text
            if r.status_code == 200:
                context['success'] = True
                
        
    return HttpResponse(json.dumps(context))







