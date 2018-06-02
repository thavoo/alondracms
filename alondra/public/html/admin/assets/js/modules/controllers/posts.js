define(['angular','clipboard'],function(angular,clipboard){
 	angular.module('app.controllers.posts', [])
 	.controller('PostsListCtrl', 
	[ '$scope','$state','$translate','Posts',
	  function ($scope,$state,$translate, Posts) 
	  {

	 
		$scope.model = {'query':'',	'currentpage':1,'pages':1,};
	  	$scope.search = function()
	  	{	
	  		$scope.model.currentpage = 1;
	  		if($scope.model.query.length > 0)
	  		{
	  			$scope.todos = [];
	  			$scope.search_list(
				    $scope.model.query,
				    $scope.model.currentpage
				);
	  		
	  		}else
	  		{
	  			$scope.makeTodos($scope.model.currentpage); 
	  		}
	  		
	  	}


	$scope.makeTodos = function(query)
		{
			$scope.todos = [];
			var query2 = typeof query === 'undefined';
			if (query2 == false)
			{
				$scope.post_list($scope.model.currentpage);
			}
			else
			{
				if($scope.model.query.length > 0)
				{
					$scope.search_list(query,$scope.model.currentpage);
				}else{
					$scope.post_list($scope.model.currentpage);
				}
				
			}
		};


		$scope.search_list = function(query,page)
		{
			
			Posts.search({
				'query':query,
				'page':page,
				'post_type':'post',
			}).then(function successCallback(response)
			{
			    $scope.model.pages = response.data.pages;
				
			    angular.forEach(response.data.items, function(value, key)
			    {
					this.push({
					 	id: value.id,
					    title: value.title,
					    img: '/admin/assets/img/logo.jpg',
					    status: value.publish,
					    created: value.created,
					    modified: value.modified,
					});
					   	
				},$scope.todos);
	       	});

		}



		$scope.post_list = function(page)
		{

		    Posts.list(page).then(function successCallback(response)
		    {
		    	$scope.model.pages = response.data.pages;
	         	angular.forEach(response.data.items, function(value, key)
	         	{
				 	this.push({
			        	id: value.id,
				        title: value.title,
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
			Posts.Delete(id).then(function successCallback(response){
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
				    $scope.search_list(
				    	$scope.model.query,
				    	$scope.model.currentpage
				    );
				}
				
				if ($scope.model.query.length == 0)
				{
				    $scope.post_list(
				    	$scope.model.currentpage
				    );
				}
				
				
			}
		}
		

		$scope.makeTodos();
		
	}]).controller('PostsEditCtrl', 
	[ '$scope','$state','$translate','$stateParams','Posts','Tags','Category','Media',
	  function ($scope,$state,$translate,$stateParams,Posts,Tags,Category,Media) 
	  {

	  	new clipboard('.btn');
	  	$scope.model = {
	  		'title':'',
	  		'adviable':true,
	  		'publish': true,
	  		'post_type': 'post',
	  		'is_featured': true,
	  		'is_on_feed': true,
	  		'publish_date': null,
	  		'thumbnail':'',
	  		'thumbnail_text':'',
	  		'featured_image':'',
            'featured_image_text':'',
	  		'categories_lists': [], 
	  		'releated_posts':[],
	  		'tags_lists': [], 
	  		'content':'',
	  		'excerpt':'',
	  		'slug':'',
	  		'meta_title':'',
	  		'meta_description':'',
	  		'query':'',	
	  		'currentpage':1,
	  		'pages':1,
	  	} 
	  	$scope.query = '';
		$scope.name = '';

	  	$scope.search = function()
	  	{	if($scope.query.length > 0)
	  		{
	  			$scope.images = $scope.images.filter(function(item){
	  				re = new RegExp($scope.query);
					return re.test(item.title) ;
				});
				
	  		}else
	  		{
	  			$scope.makeTodosMedia(); 
	  		}
	  		
	  	}
		$scope.ChangeTitle = function()
	  	{
	  		 $scope.model.meta_title = $scope.model.title
	  		 $scope.model.slug = window.string_to_slug($scope.model.title)

	  		 Posts.Find($scope.model.title).then(function successCallback(response){
				$scope.model.adviable  = response.data.adviable;
			}, function errorCallback(response) {});
	  	}

	  	Posts.Get( $stateParams.id ).then(function successCallback(response){
	  			$scope.model.title = response.data.title;
	  			$scope.model.categories_lists = response.data.categories_lists;	
	  			$scope.model.releated_posts = response.data.related_postsx;	
	  			$scope.model.tags_lists = response.data.tags_lists;	 			
	  			$scope.model.publish = response.data.publish;
	  			$scope.model.publish_date = response.data.publish_date;	 
	  			$scope.model.is_featured = response.data.is_featured;
	  			$scope.model.is_on_feed = response.data.is_on_feed;
	  			$scope.model.content = response.data.content;
	  			$scope.model.excerpt = response.data.excerpt;
	  			$scope.model.meta_title = response.data.meta_title;
	  			$scope.model.featured_image = response.data.featured_image;
	  			$scope.model.featured_image_text = response.data.featured_image_text;
	  			$scope.model.thumbnail = response.data.thumbnail;
	  			$scope.model.thumbnail_text = response.data.thumbnail_text;
	  			$scope.model.meta_description = response.data.meta_description;
	  			$scope.model.slug = response.data.slug;
	  			$scope.makeTodos();
	  			$scope.makeTodosMedia();
	  			$scope.makeTodosPosts();

			}, function errorCallback(response) {});
	  	

	  	$scope.confirmAction = function(){
	  		return Posts.Get( $stateParams.id );
	  	}

		$scope.makeTodos = function()
		{
			$scope.todos = [];
			$scope.tags = [];
		    Category.list().then(function successCallback(response)
		    {
		    	angular.forEach(response.data, function(value, key){

	         			checked =  $scope.model.categories_lists.filter(function(item){
				              	return item.id === value.id;
				          	});
					     			
					 	this.push({
				        	id: value.id,
					        title: value.name,
					        status: value.publish,
					        checked: checked.length > 0,
					        created: value.created,
					        modified: value.modified,
				      	});
			      	},$scope.todos);
        	}, function errorCallback(response) {});
        	Tags.list().then(function successCallback(response)
		    {
		    	angular.forEach(response.data, function(value, key){

	         			checked =  $scope.model.tags_lists.filter(function(item){
				              	return item.id === value.id;
				          	});
					     			
					 	this.push({
				        	id: value.id,
					        title: value.name,
					        status: value.publish,
					        checked: checked.length > 0,
					        created: value.created,
					        modified: value.modified,
				      	});
			      	},$scope.tags);
        	}, function errorCallback(response) {});
		};

	 
	  	$scope.makeTodosMedia = function()
		{
			$scope.images = [];
		    Media.list().then(function successCallback(response)
		    {
	         	angular.forEach(response.data, function(value, key){
	         	
				 	
	         		var patt = new RegExp("http\:\/\/|https\:\/\/");
	  				var res = patt.test(value.image);
	  				var image = value.image;
		  			if(res == true)
		  			{
		  				image = value.image;
		  			}else{

		  				image =  "/assets/media/" + value.image;
		  			}
				 	
				 	this.push({
			        	id: value.id,
				        title: value.title,
				        status: value.publish,
				        img: image,
				        featured_checked: value.image === $scope.model.featured_image,
				        thumb_checked: value.image === $scope.model.thumbnail,
				        created: value.created,
				        modified: value.modified,
			      	});
				},$scope.images);
        	}, function errorCallback(response) {});
		};



		$scope.featured_image = function (value) {
			featured_image = $scope.images.filter(function(item){        
              return item.id !== value.id;
          	});
          	angular.forEach(featured_image, function(value, key){

          		value.featured_checked = false;
          	})
        	
   		}
   		$scope.thumb_checked = function (value) {
			thumb = $scope.images.filter(function(item){        
              return item.id !== value.id;
          	});
          	angular.forEach(thumb, function(value, key){
          		value.thumb_checked = false;
          	});        	
   		}
	  	$scope.Save = function()
	  	{
	  		featured_image = $scope.images.filter(function(item){        
              return item.featured_checked === true;
          	});
          	thumbnail = $scope.images.filter(function(item){        
              return item.thumb_checked === true;
          	});

          	$scope.model.categories_lists = $scope.todos.filter(function(item){        
              return item.checked === true;
          	});

          	$scope.model.tag_lists = $scope.tags.filter(function(item){        
              return item.checked === true;
          	});

		  	$scope.model.id = $stateParams.id;

		  	if(featured_image.length > 0)
		  	{
		  		$scope.model.featured_image = featured_image[0].img;
		  		$scope.model.featured_image_text =  thumbnail[0].title;
		  		
		  	}
		  	if(thumbnail.length > 0)
		  	{
		  		$scope.model.thumbnail = thumbnail[0].img;
		  		$scope.model.thumbnail_text = thumbnail[0].title;
		  		
		  	}
		 	Posts.Update($scope.model);
		}


	  	$scope.search_posts = function()
	  	{	
	  		$scope.model.currentpage = 1;
	  		if($scope.model.query.length > 0)
	  		{
	  			$scope.todos2 = [];
	  			$scope.search_list(
				    $scope.model.query,
				    $scope.model.currentpage
				);
	  		
	  		}else
	  		{
	  			$scope.makeTodosPosts($scope.model.currentpage); 
	  		}
	  		
	  	}


		$scope.makeTodosPosts = function(query)
		{
			$scope.todos2 = [];
			var query2 = typeof query === 'undefined';
			if (query2 == false)
			{
				$scope.post_list($scope.model.currentpage);
			}
			else
			{
				if($scope.model.query.length > 0)
				{
					$scope.search_list(query,$scope.model.currentpage);
				}else{
					$scope.post_list($scope.model.currentpage);
				}
				
			}
		};


		$scope.search_list = function(query,page)
		{
			
			Posts.search({
				'query':query,
				'page':page,
				'post_type':'post',
				
			}).then(function successCallback(response)
			{
			    $scope.model.pages = response.data.pages;
				
			    angular.forEach(response.data.items, function(value, key)
			    {


					checked =  $scope.model.releated_posts.filter(function(item){
				              	return item === value.id;
				          	});
					this.push({
					 	id: value.id,
					    title: value.title,
					    img: '/admin/assets/img/logo.jpg',
					    selected: checked.length> 0,
					    status: value.publish,
					    created: value.created,
					    modified: value.modified,
					});
					   	
				},$scope.todos2);
	       	});

		}



		$scope.post_list = function(page)
		{

		    Posts.list(page).then(function successCallback(response)
		    {
		    	$scope.model.pages = response.data.pages;
	         	angular.forEach(response.data.items, function(value, key)
	         	{
	         		checked =  $scope.model.releated_posts.filter(function(item){
				         	return item === value.id;
				     	});
				 	this.push({
			        	id: value.id,
				        title: value.title,
				        img: '/admin/assets/img/logo.jpg',
				         selected: checked.length> 0,
				        status: value.publish,
				        created: value.created,
				        modified: value.modified,
			      	});
			      	
				},$scope.todos2);
				
        	}, function errorCallback(response) {});


		};

		$scope.selectedItem = function(item)
		{
			
			if(item.selected==false)
			{
				
				var releated_posts = $scope.model.releated_posts.filter(function(value){        
	              return item.id === value;
	          	});
	          	if(releated_posts.length == 0)
	          	{
	          		$scope.model.releated_posts.push(item.id);
	          	}
				item.selected = true;
			}else
			{
				item.selected = false;
				$scope.model.releated_posts = $scope.model.releated_posts.filter(function(value){        
	              return item.id !== value;
	          	});
			}
		};

		$scope.loadmore = function()
		{
			if($scope.model.currentpage < $scope.model.pages)
			{
				$scope.model.currentpage ++;
			
				if ($scope.model.query.length > 0)
				{
				    $scope.search_list(
				    	$scope.model.query,
				    	$scope.model.currentpage
				    );
				}
				
				if ($scope.model.query.length == 0)
				{
				    $scope.post_list(
				    	$scope.model.currentpage
				    );
				}
				
				
			}
		}
		





	}]).controller('PostsNewCtrl', 
	[ '$scope','$state','$translate','$stateParams','Posts','Tags','Category','Media',
	  function ($scope,$state,$translate,$stateParams,Posts,Tags,Category,Media) 
	  {
	  	new clipboard('.btn');
	  	$scope.model = {
	  		'title':'',
	  		'publish': true,
	  		'adviable':true,
	  		'post_type': 'post',
	  		'is_featured': true,
	  		'is_on_feed': true,
	  		'publish_date': null,
	  		'thumbnail':'',
	  		'thumbnail_text':'',
	  		'featured_image':'',
            'featured_image_text':'',
	  		'categories_lists': [], 
	  		'tags_lists': [], 
	  		'releated_posts':[],
	  		'content':'',
	  		'excerpt':'',
	  		'slug':'',
	  		'meta_title':'',
	  		'meta_description':'',
	  		'query':'',	
	  		'currentpage':1,
	  		'pages':1,
	  	} 
		$scope.query = '';
	  	$scope.search = function()
	  	{	if($scope.query.length > 0)
	  		{
	  			$scope.images = $scope.images.filter(function(item){
	  				re = new RegExp($scope.query);
					return re.test(item.title) ;
				});
				
	  		}else
	  		{
	  			$scope.makeTodosMedia(); 
	  		}
	  		
	  	}
		$scope.ChangeTitle = function()
	  	{
	  		$scope.model.meta_title = $scope.model.title;
	  		$scope.model.slug = window.string_to_slug($scope.model.title);

	  		Posts.Find($scope.model.title).then(function successCallback(response)
	  		{
				$scope.model.adviable  = response.data.adviable;
			}, function errorCallback(response) {});
	  	}
	  	$scope.Save = function()
	  	{
	  		$scope.model.categories_lists = $scope.todos.filter(function(item){
              	return item.checked === true;
          	});
          	$scope.model.tag_lists = $scope.tags.filter(function(item){        
              return item.checked === true;
          	});
	  		Posts.New($scope.model).then(function successCallback(response)
		    {
		    	$state.go('root.post_edit',{'id':response.data.id});

		    }, function errorCallback(response) {});;
	  	}
		$scope.makeTodosMedia = function()
		{
			$scope.images = [];
		    Media.list().then(function successCallback(response)
		    {
	         	angular.forEach(response.data, function(value, key){
				 	this.push({
			        	id: value.id,
				        title: value.title,
				        status: value.publish,
				        img:  value.image,
				        created: value.created,
				        modified: value.modified,
			      	});
				},$scope.images);
        	}, function errorCallback(response) {});
		};

		$scope.makeTodos = function()
		{
			$scope.todos = [];
			$scope.tags = [];
		    Category.list().then(function successCallback(response)
		    {
	         	angular.forEach(response.data, function(value, key){
				 	this.push({
			        	id: value.id,
				        title: value.name,
				        status: value.publish,
				        checked: false,
				        created: value.created,
				        modified: value.modified,
			      	});

				},$scope.todos);
				
        	}, function errorCallback(response) {});
        	
			Tags.list().then(function successCallback(response)
		    {
		    	angular.forEach(response.data, function(value, key){

	         			checked =  $scope.model.tags_lists.filter(function(item){
				              	return item.id === value.id;
				          	});
					     			
					 	this.push({
				        	id: value.id,
					        title: value.name,
					        status: value.publish,
					        checked: checked.length > 0,
					        created: value.created,
					        modified: value.modified,
				      	});
			      	},$scope.tags);
        	}, function errorCallback(response) {});
		};

	  	$scope.search_posts = function()
	  	{	

	  		$scope.model.currentpage = 1;
	  		if($scope.model.query.length > 0)
	  		{
	  			$scope.todos2 = [];
	  			$scope.search_list(
				    $scope.model.query,
				    $scope.model.currentpage
				);
	  		
	  		}else
	  		{
	  			$scope.makeTodosPosts($scope.model.currentpage); 
	  		}
	  		
	  	}

		$scope.makeTodosPosts = function(query)
		{
			$scope.todos2 = [];
			var query2 = typeof query === 'undefined';
			if (query2 == false)
			{
				$scope.post_list($scope.model.currentpage);
			}
			else
			{
				if($scope.model.query.length > 0)
				{
					$scope.search_list(query,$scope.model.currentpage);
				}else{
					$scope.post_list($scope.model.currentpage);
				}
				
			}
		};

		$scope.selectedItem = function(item)
		{
			
			if(item.selected==false)
			{
				
				var releated_posts = $scope.model.releated_posts.filter(function(value){        
	              return item.id === value;
	          	});
	          	if(releated_posts.length == 0)
	          	{
	          		$scope.model.releated_posts.push(item.id);
	          	}
				item.selected = true;
			}else
			{
				item.selected = false;
				$scope.model.releated_posts = $scope.model.releated_posts.filter(function(value){        
	              return item.id !== value;
	          	});
			}
		};


		$scope.search_list = function(query,page)
		{
			
			Posts.search({
				'query':query,
				'page':page,
				'post_type':'post',
			}).then(function successCallback(response)
			{
			    $scope.model.pages = response.data.pages;
				
			    angular.forEach(response.data.items, function(value, key)
			    {
					this.push({
					 	id: value.id,
					    title: value.title,
					    img: '/admin/assets/img/logo.jpg',
					    selected: false,
					    status: value.publish,
					    created: value.created,
					    modified: value.modified,
					});
					   	
				},$scope.todos2);
	       	});

		}



		$scope.post_list = function(page)
		{

		    Posts.list(page).then(function successCallback(response)
		    {
		    	$scope.model.pages = response.data.pages;
	         	angular.forEach(response.data.items, function(value, key)
	         	{
				 	this.push({
			        	id: value.id,
				        title: value.title,
				        img: '/admin/assets/img/logo.jpg',
				        selected: false,
				        status: value.publish,
				        created: value.created,
				        modified: value.modified,
			      	});
			      	
				},$scope.todos2);
				
        	}, function errorCallback(response) {});


		};

		$scope.loadmore = function()
		{
			if($scope.model.currentpage < $scope.model.pages)
			{
				$scope.model.currentpage ++;
			
				if ($scope.model.query.length > 0)
				{
				    $scope.search_list(
				    	$scope.model.query,
				    	$scope.model.currentpage
				    );
				}
				
				if ($scope.model.query.length == 0)
				{
				    $scope.post_list(
				    	$scope.model.currentpage
				    );
				}
				
				
			}
		}
		





	  	$scope.makeTodos();
	  	$scope.makeTodosPosts();
	  	$scope.makeTodosMedia();




	}]);
  
});


