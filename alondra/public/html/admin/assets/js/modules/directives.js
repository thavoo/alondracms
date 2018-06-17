define(['angular','jquery'],function(angular,query){

  angular.module('app.directives', [])
  .directive('blankDirective', [function(){}])
  .directive('showTab', function () {
    return {
      link: function (scope, element, attrs) {
        element.click(function (e) {
          e.preventDefault();
          query(element).tab('show');
        });
      }
    };
  }).directive('userNav', [function() 
  {
    return{   
      templateUrl: '/admin/assets/js/modules/templates/includes/usernav.html',
      restrict: 'EC',
      replace: true
    };
  }]).directive('userSearch', [function() 
  {
    return{   
      templateUrl: '/admin/assets/js/modules/templates/includes/search.html',
      restrict: 'EC',
      replace: true
    };
  }])
  .directive('headerNav', [function() 
  {
    return{   
      templateUrl: '/admin/assets/js/modules/templates/includes/header.html',
      restrict: 'EC',
      replace: true,
      controller: ['$scope', function ($scope) {

        window.app.init();    
        window.app.layout();
        window.app.spy();
        window.app.resizableLayout();           
         
        window.app.navigation();        
        window.app.navigationMobile();
        window.app.contentTabs();    
        window.app.formsFile();
        window.app.checkAll();
        window.app.loaded();

        query(window).resize(function()
        {        
          
          delayBeforeFire(function(){
              window.app.accordionFullHeightResize();
              window.app.features.gallery.controlHeight();
              window.app.spy();
          },100);
          
        });

        window.app_plugins.checkbox_radio();
        window.app_plugins.formSpinner();
        window.app_plugins.switch_button();
        window.app_plugins.bootstrap_select();
        window.app_plugins.select2();
        window.app_plugins.bootstrap_popover();
        window.app_plugins.bootstrap_datepicker();
        window.app_plugins.bootstrap_tooltip();
        window.app_plugins.maskedInput();
        window.app_plugins.datatables();
        window.app_plugins.knob();
        window.app_plugins.sparkline();
        window.app_plugins.isotope();
        window.app_plugins.noty();
        window.app_plugins.wizard();
        window.app_plugins.bootstrap_daterange();
        window.app_plugins.multiselect();
        window.app_plugins.bootstrap_colorpicker();
              

        window.app_demo.googlemap();
        window.app_demo.jvectormap();
        window.app_demo.solutions.bank.change_password();
        window.app_demo.solutions.bank.change_pin();
        window.app_demo.charts.morris();
        window.app_demo.charts.rickshaw();
        window.app_demo.charts.chartjs();
        window.app_plugins.Dropzone();
      }]
    };
  }])

  .directive('runDashboard', [function() 
  {
    return{   
      templateUrl: '/admin/assets/js/modules/templates/includes/dashboardloaded.html',
      restrict: 'EC',
      replace: true,
      controller: ['$scope', function ($scope) {


        window.app.init();    
        window.app.layout();
        window.app.spy();
        window.app.resizableLayout();           
         
        window.app.navigation();        
        window.app.navigationMobile();
        window.app.contentTabs();    
        window.app.formsFile();
        window.app.checkAll();
        window.app.loaded();

        query(window).resize(function()
        {        
          
          delayBeforeFire(function(){
              window.app.accordionFullHeightResize();
              window.app.features.gallery.controlHeight();
              window.app.spy();
          },100);
          
        });

        window.app_plugins.checkbox_radio();
        window.app_plugins.formSpinner();
        window.app_plugins.switch_button();
        window.app_plugins.bootstrap_select();
        window.app_plugins.select2();
        window.app_plugins.bootstrap_popover();
        window.app_plugins.bootstrap_datepicker();
        window.app_plugins.bootstrap_tooltip();
        window.app_plugins.maskedInput();
        window.app_plugins.datatables();
        window.app_plugins.knob();
        window.app_plugins.sparkline();
        window.app_plugins.isotope();
        window.app_plugins.noty();
        window.app_plugins.wizard();
        window.app_plugins.bootstrap_daterange();
        window.app_plugins.multiselect();
        window.app_plugins.bootstrap_colorpicker();
              

        window.app_demo.googlemap();
        window.app_demo.jvectormap();
        window.app_demo.solutions.bank.change_password();
        window.app_demo.solutions.bank.change_pin();
        window.app_demo.charts.morris();
        window.app_demo.charts.rickshaw();
        window.app_demo.charts.chartjs();
        window.app_plugins.Dropzone();
      }]
    };
  }]).directive('headingNav', [function() 
  {
    return{   
      templateUrl: '/admin/assets/js/modules/templates/includes/heading.html',
      restrict: 'EC',
      replace: true
    };
  }]).directive('sidebarNav', [function() 
  {
    return{   
      templateUrl: '/admin/assets/js/modules/templates/includes/sidebar.html',
      restrict: 'EC',
      replace: true
    };
  }]).directive('footerNav', [function() 
  {
    return{   
      templateUrl: '/admin/assets/js/modules/templates/includes/footer.html',
      restrict: 'EC',
      replace: true
    };
  }]);
  
});
