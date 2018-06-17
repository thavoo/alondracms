define(['angular'],function(angular){
 	angular.module('app.controllers.tags', [])
 	.controller('TagsListCtrl', 
	[ '$scope','$state','$translate','Tags',
	  function ($scope,$state,$translate, Tags) 
	  {

		$scope.model = {'query':'',	'currentpage':1,'pages':1,};
	  	$scope.search = function()
	  	{	
	  		$scope.todos = [];
	  		$scope.model.currentpage = 1;
	  		if($scope.model.query.length > 0)
	  		{
	  			$scope.search_list();
	  		}else
	  		{
	  			$scope.post_list();
	  		}
	  		
	  	}


		$scope.makeTodos = function()
		{
			$scope.todos = [];
			$scope.model.currentpage = 1;
			$scope.post_list();
		};


	
		$scope.search_list = function()
		{
			
			Tags.search({
				'query': $scope.model.query,
				'page':	$scope.model.currentpage,
				'post_type':'Tags',
			}).then(function successCallback(response)
			{
			    $scope.model.pages = response.data.pages;
				
			    angular.forEach(response.data.items, function(value, key)
			    {
					this.push({
					 	id: value.id,
					    title: value.name,
					    img: '/admin/assets/img/logo.jpg',
					    status: value.publish,
					    created: value.created,
					    modified: value.modified,
					});
					   	
				},$scope.todos);
	       	});

		}



		$scope.post_list = function()
		{
		    Tags.list($scope.model.currentpage).then(function successCallback(response)
		    {
		    	$scope.model.pages = response.data.pages;
	         	angular.forEach(response.data.items, function(value, key)
	         	{
				 	this.push({
			        	id: value.id,
				        title: value.name,
				        img: '/admin/assets/img/logo.jpg',
				        status: value.publish,
				        created: value.created,
				        modified: value.modified,
			      	});
			      	
				},$scope.todos);
				
        	}, function errorCallback(response) {});
		};

		$scope.DELETE = function(id)
		{
			Tags.Delete(id).then(function successCallback(response){
				$scope.makeTodos(); 
			}, function errorCallback(response) {});
		}


		$scope.loadmore = function()
		{
			if($scope.model.currentpage < $scope.model.pages)
			{
				$scope.model.currentpage ++;
			
				if ($scope.model.query.length > 0)
				{
				    $scope.search_list();
				}
				
				if ($scope.model.query.length == 0)
				{
				    $scope.post_list();
				}
			}
		}
		

		$scope.makeTodos();
	}]).controller('TagsEditCtrl', 
	[ '$scope','$state','$translate','$stateParams','Tags',
	  function ($scope,$state,$translate,$stateParams,Tags) 
	  {

	  	$scope.model = { 
	  		'name':'', 
	  		'publish': true,
	  		'slug':'',
	  		'meta_title':'',
	  		'meta_description':''
	  	} 

	  	
	  	$scope.ChangeTitle = function()
	  	{
	  		 $scope.model.meta_title = $scope.model.name
	  		 $scope.model.slug = window.string_to_slug($scope.model.name)
	  	}


	  	Tags.Get( $stateParams.id ).then(function successCallback(response){
	  			$scope.model.name = response.data.name;
	  			$scope.model.publish = response.data.publish;
	  			$scope.model.content = response.data.content;
	  			$scope.model.meta_title = response.data.meta_title;
	  			$scope.model.meta_description = response.data.meta_description;
	  			$scope.model.slug = response.data.slug;

			}, function errorCallback(response) {});
	  	
	  	$scope.save = function()
	  {
	  	$scope.model.id = $stateParams.id;
	  	Tags.Update($scope.model);
	  }

	}]).controller('TagsNewCtrl', 
	[ '$scope','$state','$translate','Tags',
	  function ($scope,$state,$translate, Tags) 
	  {

	  	$scope.model = {
	  		'name':'',
	  		'publish': true,
	  		'slug':'',
	  		'meta_title':'',
	  		'meta_description':''
	  	} 

	  	$scope.ChangeTitle = function()
	  	{
	  		 $scope.model.meta_title = $scope.model.name
	  		 $scope.model.slug = window.string_to_slug($scope.model.name)
	  	}

	  	$scope.save = function()
		{
		  
		  	Tags.New($scope.model).then(function successCallback(response)
		    {
		    	$state.go('root.tags_edit',{'id':response.data.id});

		    }, function errorCallback(response) {});;;
		}

	 
	  

	}]);
  
});


