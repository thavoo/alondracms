
from django.conf.urls import url
from posts import views 
# Create your views here.
urlpatterns = [
    
  
    url(r'^category/(?P<slug>[0-9A-Za-z-_]+)/{0,1}$',
            views.category,
            name='category'
        ),
    url(r'^category/(?P<slug>[0-9A-Za-z-_]+)/page/(?P<page>\d+)/{0,1}$',
            views.category,
            name='category'
        ),

    url(r'^search/{0,1}$',
            views.search,
            name='search'
        ),

    url(r'^search/page/(?P<page>\d+)/{0,1}$',
            views.search,
            name='search'
        ),

    url(r'^autor/(?P<slug>[0-9A-Za-z-_]+)/page/(?P<page>\d+)/{0,1}$',
        views.autor,
        name='posts_autor'
    ),

    url(r'^autor/(?P<slug>[0-9A-Za-z-_]+)/{0,1}$',
           views.autor,
           name='posts_autor'
    ),
    
    url(r'^tag/(?P<slug>[0-9A-Za-z-_]+)/page/(?P<page>\d+)/{0,1}$',
        views.tags,
        name='posts_tags'
    ),

    url(r'^tag/(?P<slug>[0-9A-Za-z-_]+)/{0,1}$',
           views.tags,
           name='posts_tags'
    ),



    url(r'^archive/(?P<year>[0-9A-Za-z-_]+)/(?P<month>[0-9A-Za-z-_]+)/page/(?P<page>\d+)/{0,1}$',
        views.year_month_archive,
        name='year_month_archive'
    ),

    url(r'^archive/(?P<year>[0-9A-Za-z-_]+)/(?P<month>[0-9A-Za-z-_]+)/{0,1}$',
           views.year_month_archive,
           name='year_month_archive'
    ),



    
]