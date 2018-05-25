define(['angular','jquery'],function(angular,jquery){
 	angular.module('app.controllers.navigation_items', [])
	.controller('NavigationItemEditCtrl', 
	[ '$scope','$state','$interval','$translate','$stateParams','Navigation','NavigationItems',
	  function ($scope,$state,$interval,$translate,$stateParams,Navigation, NavigationItems) 
	  {


	  	$scope.model = { 
	  		'title':'',
	  		'link': '',
	  		'image': '',
	  		'id': $stateParams.id
	  	} 


	  	NavigationItems.Get( $stateParams.id ).then(function successCallback(response){
	  			$scope.model.title = response.data.title;
	  			$scope.model.link = response.data.link;
	  			$scope.model.image = response.data.image;
			}, function errorCallback(response) {});
	  	
	  	$scope.Save = function()
		{
		  	$scope.model.id = $stateParams.id;
		  	NavigationItems.Update($scope.model);
		}
	
	}]).controller('NavigationItemNewCtrl', 
	[ '$scope','$state','$stateParams','$translate','Posts','Category','Navigation','NavigationItems',
	  function ($scope,$state,$stateParams,$translate,Posts,Category,Navigation,NavigationItems) 
	  {


	  	$scope.model = {
	  		'title':'',
	  		'link': '',
	  		'image': '',
	  		'position': $stateParams.parent
	  	}


        $scope.Save = function(){
        	NavigationItems.New($scope.model).then(function successCallback(response)
		    {
		    	$state.go('root.navigation_item_edit',{'id':response.data.id});

		    }, function errorCallback(response) {});;;
	  	}
      
	}]);
  
});
