
from django.conf.urls import url
from game import views 
# Create your views here.
urlpatterns = [
    
  
    url(r'^juegos/{0,1}$',
            views.games,
            name='games'
        ),
    url(r'^juegos/(?P<page>\d+)/{0,1}$',
            views.games,
            name='games'
        ),


    url(r'^juego/(?P<slug>[0-9A-Za-z-_]+)/{0,1}$',
           views.game,
           name='game'
    ),
    
    url(r'^juego/rating/(?P<slug>[0-9A-Za-z-_]+)/{0,1}$',
           views.game_rating,
           name='game_rating'
    ),
    url(r'^juego/rate/(?P<slug>[0-9A-Za-z-_]+)/{0,1}$',
           views.rate_game,
           name='rate_game'
    ),
    
    




    
]