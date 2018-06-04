from django.conf.urls import url
from email_suscription import views 
# Create your views here.
urlpatterns = [
    
  
    url(r'^suscribe/email/{0,1}$',
            views.suscribe_to_serivice,
            name='suscribe_to_serivice'
        ),
   
    
]