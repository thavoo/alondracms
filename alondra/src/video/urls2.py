
from django.conf.urls import url
from video import views 
# Create your views here.
urlpatterns = [
    
  
    url(r'^videos/{0,1}$',
            views.videos,
            name='videos'
        ),
    url(r'^videos/(?P<page>\d+)/{0,1}$',
            views.videos,
            name='videos'
        ),


    url(r'^video/(?P<slug>[0-9A-Za-z-_]+)/{0,1}$',
           views.video,
           name='video'
    ),
 

    
]