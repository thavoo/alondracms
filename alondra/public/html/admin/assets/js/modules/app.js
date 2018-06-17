define(
    [
      "angular",
      "router",
      "app_boostrap"
    ],

    function (angular)
    {
      var app = angular.module('app', [
        'ui.router',
        'bw.paging',
        'ngCookies',
        'cms-simplemde',
        'dropzone',
        'datepicker',
        'pascalprecht.translate', 
        'app.directives',
        'app.directives.login',
        'app.directives.fileupload',
        'app.controllers.posts',
        'app.controllers.pages',
        'app.controllers.category',
        'app.controllers.tags',
        'app.controllers.comments',
        'app.controllers.media',
        'app.controllers.media_album',
        'app.controllers.users',
        'app.controllers.groups',
        'app.controllers.themes',        
        'app.controllers.login',
        'app.controllers.navigation',
        'app.controllers.navigation_items',
        'app.services.user',
        'app.services.login',
        'app.services.posts',
        'app.services.pages',
        'app.services.tags',
        'app.services.category',
        'app.services.comments',
        'app.services.media',
        'app.services.media_album',
        'app.services.navigation',
        'app.services.navigation_items',
        'app.routes.posts',
        'app.routes.pages',
        'app.routes.media',
        'app.routes.media_album',
        'app.routes.users',
        'app.routes.category',
        'app.routes.tags',
        'app.routes.comments',
        'app.routes.groups',
        'app.routes.themes',
        'app.routes.root',
        'app.routes.login',
        'app.routes.navigation',
        'app.I18N.EN',
        'app.I18N.ES',
      ]);
      
   
      app.run([
        '$rootScope', '$state','$http', '$stateParams', '$interval','Login',
        function ($rootScope, $http,  $state, $stateParams,$interval,Login) 
        {
         
          $rootScope.$state = $state;

          $rootScope.$stateParams = $stateParams;
     

          $rootScope.$on('$includeContentLoaded', function(){
          

          });
          $rootScope.$on('$viewContentLoaded', function() {
            
          });
          $rootScope.$on('$stateChangeStart', function (event, toState, toParams, fromState, fromParams){
           
             
              contains = [
                'login.screen',
                'login',
                'login.screen',
                'login.registration',             
                'login.forgot',
                'login.new_password',
              ];

          });
        }
      ]);
    
      app.config([
      '$stateProvider', '$urlRouterProvider',"$locationProvider",'$translateProvider','$httpProvider','$cookiesProvider','$qProvider',
      function($stateProvider, $urlRouterProvider, $locationProvider,$translateProvider,$httpProvider,$cookiesProvider,$qProvider)
      {
        $urlRouterProvider.otherwise('/login');
        $cookiesProvider.defaults.path = "/";
        $translateProvider.useSanitizeValueStrategy('sanitizeParameters');
        $translateProvider.preferredLanguage('es');
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $qProvider.errorOnUnhandledRejections(false);
      }]);
      
      app.bootstrap = function () {
        angular.bootstrap(document, ['app']);
      }
     
      return app;
   
});