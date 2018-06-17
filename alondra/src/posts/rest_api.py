import json
from django.conf import settings
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets, generics
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import generics
from posts.models import PostCategory
from posts.models import PostItem
from globaly.models import GlobalyTags
from globaly.rest_api import GlobalyTagsSerializer
from media.models import MediaAlbum,MediaImage
from django.contrib.auth.models import User
from user.rest_authentication import IsAuthenticated
from django.db.models import Q
from decimal import Decimal as D
from django.db.models import Max
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from navigation.models import NavigationItem
from utilities.paginator import paginator

class PostCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostCategory
        fields =    (
            'id', 
            'name',
            'slug',
            'meta_title',
            'meta_description',
            'publish',
            'post_type', 
            'created', 
            'modified',
        )

class PostItemSerializer(serializers.HyperlinkedModelSerializer):
    categories_lists = PostCategorySerializer(source='categories', many=True, read_only = True)
    tags_lists = GlobalyTagsSerializer(source='tags', many=True, read_only = True)
    autor_id = serializers.ReadOnlyField(source='autor.id')
    related_postsx = serializers.SerializerMethodField('get_popularity')
    class Meta:
        model = PostItem
        fields = (
            'id',
            'autor_id',
            'categories_lists',
            'related_postsx',
            'tags_lists',
            'title',
            'slug',
            'meta_title',
            'meta_description',
            'publish',
            'thumbnail',
            'thumbnail_text',
            'featured_image',
            'featured_image_text',
            'content',
            'excerpt',
            'publish_date',
            'featured_start_date',
            'featured_end_date',
            'post_type',
            'is_featured',
            'is_on_feed',
        )
 
    def get_popularity(self, ob):
        
        return ob.RelatedPosts()
 
@api_view(['POST'])
def post_list(request):
        
    if request.method == 'POST':
        page = int(request.data.get('page',1))
        post_type = request.data.get('post_type','post')
        
       
        f3 = Q(post_type=post_type ) 
        posts = paginator(
                page, 
                PostItem.objects.filter(f3).order_by('-id'),
                100
            )
        
        serializer = PostItemSerializer(
            posts, 
            many=True,
            context={'request': request}
        )
        next_page = 0
        previous_page = 0
        if posts.has_next():
            next_page = posts.next_page_number()
        if posts.has_previous():
            previous_page = posts.previous_page_number()

        return Response({
            'pages':posts.paginator.num_pages,
            'items':serializer.data,
            'next_page':next_page,
            'previous_page':previous_page,
        })

@api_view(['POST'])
def search_list(request):
        
    if request.method == 'POST':
       
        query = request.data.get('query',None)
        page = int(request.data.get('page',1))
        post_type = request.data.get('post_type','post')
        
        f1 = Q()
       
        f4 = Q(post_type=post_type)
        if(query is not None):
            f1 = Q(title__icontains=query)
        posts = paginator(
                page, 
                PostItem.objects.filter(f1 & f4).order_by('-id'),
                100
            )

         
        serializer = PostItemSerializer(
            posts, 
            many=True,
            context={'request': request}
        )
        next_page = 0
        previous_page = 0
        if posts.has_next():
            next_page = posts.next_page_number()
        if posts.has_previous():
            previous_page = posts.previous_page_number()

        return Response({
            'pages':posts.paginator.num_pages,
            'items':serializer.data,
            'next_page':next_page,
            'previous_page':previous_page,
        })
    return Response(
                status=status.HTTP_204_NO_CONTENT
            )


@api_view(['POST'])
@permission_classes((AllowAny,))
def search_list_published(request):
        
    if request.method == 'POST':
       
        query = request.data.get('query',None)
        page = int(request.data.get('page',1))
        post_type = request.data.get('post_type','post')
        limit = request.data.get('limit',100)
        
        f1 = Q()
       
        f4 = Q(post_type=post_type)
        f5 = Q(publish=True)
        if(query is not None):
            f1 = Q(title__icontains=query)
            if(query.isdigit() == True):
                f1 = Q(id=int(query))
        
        posts = paginator(
                page, 
                PostItem.objects.filter(f1 & f4 & f5).order_by('-id'),
                limit
            )

         
        serializer = PostItemSerializer(
            posts, 
            many=True,
            context={'request': request}
        )
        next_page = 0
        previous_page = 0
        if posts.has_next():
            next_page = posts.next_page_number()
        if posts.has_previous():
            previous_page = posts.previous_page_number()

        return Response({
            'pages':posts.paginator.num_pages,
            'items':serializer.data,
            'next_page':next_page,
            'previous_page':previous_page,
        })
    return Response(
                status=status.HTTP_204_NO_CONTENT
            )


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def post_details(request):
    if request.method == 'POST':
        try:
            pk = request.data.get('id')
            post = PostItem.objects.get(
                pk=pk
            )
        except PostItem.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PostItemSerializer(
            post,
            context={'request': request}
        )
        return Response(serializer.data)
    return Response(
                status=status.HTTP_204_NO_CONTENT
            )

@api_view(['PUT','POST','DELETE'])
@permission_classes((IsAuthenticated,))
def post(request):
    
    if request.method == 'POST':
        serializer = PostItemSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
              
            serializer.save(autor=request.user)
            if request.data.has_key('categories_lists'):
               
                d = request.data['categories_lists']
                data = [ value.get('id') for value in d]
                categories = PostCategory.objects.filter(                   
                    pk__in=data
                )
                serializer.save(
                    categories=categories                      
                )

            if request.data.has_key('tag_lists'):
                t = request.data['tag_lists']
                data = [ value.get('id') for value in t]
                tags = GlobalyTags.objects.filter(                   
                    pk__in=data
                )
                serializer.save(
                   tags=tags                     
                )
            if request.data.has_key('releated_posts'):
                t = request.data['releated_posts']
                data = [ value for value in t]
                related_posts = PostItem.objects.filter(                   
                    pk__in=data
                )
                serializer.save(
                   related_posts=related_posts                     
                )

                

            return Response(serializer.data)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )      
    if request.method == 'PUT' or request.method == 'DELETE':
        try:
            pk = request.data.get('id')
            post = PostItem.objects.get(
                pk=int(pk)
            )
        except PostItem.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        if request.method == 'PUT':
            serializer = PostItemSerializer(
                post,
                data=request.data,
                context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                if request.data.has_key('categories_lists'):
                   
                    d = request.data['categories_lists']
                    data = [ value.get('id') for value in d]
                    categories = PostCategory.objects.filter(                   
                        pk__in=data
                    )
                    serializer.save(
                        categories=categories                      
                    )

                if request.data.has_key('tag_lists'):
                    t = request.data['tag_lists']
                    data = [ value.get('id') for value in t]
                    tags = GlobalyTags.objects.filter(                   
                        pk__in=data
                    )
                    serializer.save(
                       tags=tags                     
                    )
                if request.data.has_key('releated_posts'):
                    t = request.data['releated_posts']
                    data = [ value for value in t]
                    related_posts = PostItem.objects.filter(                   
                        pk__in=data
                    )
                    serializer.save(
                       related_posts=related_posts                     
                    )

               
                return Response(serializer.data)

        if request.method == 'DELETE':
            post.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )

    return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )    

@api_view(['POST'])
def find_post(request):
    if request.method == 'POST':
        try:
            title = request.data.get('name')
            adspackages = PostItem.objects.get(
                title=title,
                post_type='post',
            )
            return Response(
                {'adviable':False}
            )
        except PostItem.DoesNotExist:
            return Response(
                {'adviable':True}
            )
    return Response(
                status=status.HTTP_204_NO_CONTENT
            )


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def categories_list(request):

    if request.method == 'GET':
        posts = PostCategory.objects.all().order_by('-id')
        serializer = PostCategorySerializer(
            posts, 
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def category_details(request):
    if request.method == 'POST':
        try:
            pk = request.data.get('id')
            category = PostCategory.objects.get(
                pk=pk
            )
        except PostCategory.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PostCategorySerializer(
            category,
            context={'request': request}
        )
        return Response(serializer.data)
    return Response(
                status=status.HTTP_204_NO_CONTENT
            )


@api_view(['PUT','POST','DELETE'])
@permission_classes((IsAuthenticated,))
def category(request):
    
    if request.method == 'POST':
        serializer = PostCategorySerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )      
    if request.method == 'PUT' or request.method == 'DELETE':
        try:
            pk = request.data.get('id')
            category = PostCategory.objects.get(
                pk=int(pk)
            )
        except PostCategory.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        if request.method == 'PUT':
            serializer = PostCategorySerializer(
                category,
                data=request.data,
                context={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

        if request.method == 'DELETE':
            category.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )

    return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )    
