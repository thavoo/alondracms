from django.core.urlresolvers import resolve
from django.http import HttpResponseForbidden
import importlib
from django.http import Http404
from posts.models import PostCategory
from posts.models import PostItem
from django.utils import timezone
from django.db.models import Q

class BlogUrlsMiddleware(object):
    

    def get_my_view (self, model):
        app_label =  model._meta.app_label
        name = 'src.%s.views' % app_label
        module = importlib.import_module(name)
                        
        return getattr(module, model.view_name)

    def process_view(self, request, view_func, view_args, view_kwargs):
       
        request.name = view_kwargs.get ('name', None)
        current_url = resolve(request.path_info)
        url_name = current_url.url_name
        current_date =  timezone.now()
        if  url_name == 'page_details': 
            if view_kwargs.has_key('slug'):
                f1 = Q(publish=True)
                f2 = Q(publish_date__lte=current_date)
                f3 = Q(publish_date=None) 
                f4 = Q(slug=view_kwargs.get('slug'))

                try:
                    model = PostCategory.objects.get( f1 & f4 )
                    view_kwargs['model'] = model
                    view_func = self.get_my_view(model)
                    return view_func(request, *view_args, **view_kwargs)

                except PostCategory.DoesNotExist:
                    try:
                        model = PostItem.objects.get( f1 & (f2 | f3) & f4)
                        view_kwargs['model'] = model
                        
                        view_func = self.get_my_view(model)
                        return view_func(request, *view_args, **view_kwargs)
                    except PostItem.DoesNotExist:
                        pass
                raise Http404



BotNames=['Googlebot','Slurp','Twiceler','msnbot','KaloogaBot','YodaoBot','"Baiduspider','googlebot','Speedy Spider','DotBot']
param_name='deny_crawlers'

class CrawlerBlocker:
    def process_request(self, request):
        user_agent=request.META.get('HTTP_USER_AGENT',None)
        
        if not user_agent:
            return HttpResponseForbidden('request without username are not supported. sorry')
        request.is_crawler=False
        
        for botname in BotNames:
            if botname in user_agent:
                request.is_crawler=True
                
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if param_name in view_kwargs:
            if view_kwargs[param_name]:
                del view_kwargs[param_name]
                if request.is_crawler:
                    return HttpResponseForbidden('adress removed from crawling. check robots.txt')



