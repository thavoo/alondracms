

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

TIME_ZONE = 'America/Caracas'

APPEND_SLASH = True

SECRET_KEY = 'nv-=_gl5d(^vd05=9waomq%n_m%=(j98zesf^@$$@erz7-k=j5'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'info@webdisenoya.com'
EMAIL_HOST_PASSWORD = 'yaverioX36'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL= 'info@webdisenoya.com'
DEFAULT_TO_EMAIL_LIST = ['info@webdisenoya.com']

EXCLUDE_AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

AUTHENTICATION_BACKENDS = ( 
    #'user_site.backends.UserSiteBackend',
    #'user_site.backends.UserAuthAdminEmailBackend',  
    'user.backends.CustomUserBackend',  
    'django.contrib.auth.backends.ModelBackend',    
)

TOP_RATED_GAMES = 'http://database.gamajuegos.com/api/games/new/launched/'
GET_GAME = 'http://database.gamajuegos.com/api/game/get/'

GAMES_LIST = 'http://database.gamajuegos.com/api/games/'


VIDEOS_LIST = 'http://videodatabase.gamajuegos.com/api/posts/'

GET_VIDEO = 'http://videodatabase.gamajuegos.com/api/post/parent/list/'

GET_VIDEO_PARENT_LIST = 'http://videodatabase.gamajuegos.com/api/list/parent/'

GET_VIDEO_RELATED_LIST = 'http://videodatabase.gamajuegos.com/api/post/related/list/'

GET_VIDEO_DETAILS = 'http://videodatabase.gamajuegos.com/api/post/get/'
	
GET_IMAGES_RELATED_LIST = 'http://imagesdatabase.gamajuegos.com/api/post/parent/list/'