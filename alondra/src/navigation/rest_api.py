import json
from django.conf import settings
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets, generics
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from navigation.models import NavigationPosition
from user_site.models import UserSite
from django.contrib.auth.models import User
from navigation.models import NavigationItem
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from user.rest_authentication import IsAuthenticated,IsSuperUser
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_recursive.fields import RecursiveField

class NavigationPositionSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = NavigationPosition
        fields =    (
            'id', 
            'name',
            'publish', 
            'created', 
            'modified',
        )


class NavigationItemSerializer(serializers.HyperlinkedModelSerializer):
 
    parent_id = serializers.ReadOnlyField(source='parent.id') 
    parent = serializers.ListField(read_only=True,child=RecursiveField(),source="get_descendants")
    class Meta:
        model = NavigationItem
        fields =    (
            'id',
            'link',
            'image',
            'title',
            'created',
            'parent',
            'modified',
            'parent_id',
        )

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def nav_list(request):
        
    if request.method == 'GET':
        navigation = NavigationPosition.objects.all()
        serializer = NavigationPositionSerializer(
            navigation, 
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def nav(request):
    if request.method == 'POST':
        try:
            pk = request.data.get('id')
            navigation = NavigationPosition.objects.get(
                pk=pk
            )
        except NavigationPosition.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = NavigationPositionSerializer(
            navigation,
            context={'request': request}
        )
        return Response(serializer.data)
    return Response(
                status=status.HTTP_204_NO_CONTENT
            )



@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def nav_details(request):
    pk = request.data.get('id', None)
    navigations = request.data.get('navigation', [])
    children_in_parent = []
    for nav in navigations:
    
        if (nav.has_key('children')):
            for children in nav.get('children'):

               

                try:
                    parent = NavigationItem.objects.get(
                        pk=int(nav.get('id'))
                    )
                    try:
                        child = NavigationItem.objects.get(
                             pk=int(children.get('id'))
                        )
                        child.parent = parent

                        child.save()
                        children_in_parent.append(int(children.get('id')))
                    except NavigationItem.DoesNotExist:
                        pass
                except NavigationItem.DoesNotExist:
                    pass
                    print "no existe"
        
        for child in NavigationItem.objects.filter(parent__pk=int(nav.get('id'))):
            
            if child.parent.id == int(nav.get('id')) and child.id not in children_in_parent:
                
                child.parent = None
                child.save()               
                           
    if pk is not None:
        try:
            navigation = NavigationPosition.objects.get(
                pk=pk
            )
        except NavigationPosition.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
     
    if request.method == 'POST':
        serializer = NavigationPositionSerializer(
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
    elif request.method == 'PUT':
        serializer = NavigationPositionSerializer(
            navigation, 
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()    
            return Response(serializer.data)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )    
    if request.method == 'DELETE':
        navigation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def nav_item_list(request):
        
    if request.method == 'POST':
        pk = request.data.get('id')
        navigation = NavigationItem.objects.filter(
            parent=None,
            position__id=pk
        )
        serializer = NavigationItemSerializer(
            navigation, 
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def nav_item_details(request):

    if request.method == 'POST':
        try:
            pk = request.data.get('id')
            navigation = NavigationItem.objects.get(
                pk=pk
            )
        except NavigationItem.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = NavigationItemSerializer(
            navigation,
            context={'request': request}
        )
        return Response(serializer.data)
    return Response(
                status=status.HTTP_204_NO_CONTENT
            )

@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def nav_item(request):
    pk = request.data.get('id', None)
    if pk is not None:
        try:
            navigation = NavigationItem.objects.get(
                pk=pk
            )
        except NavigationItem.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
 
    if request.method == 'POST':
        try:
            pk = request.data.get('position')
            navigation_pos = NavigationPosition.objects.get(
                pk=pk
            )
        except NavigationPosition.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = NavigationItemSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(position=navigation_pos)
            return Response(serializer.data)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )      
    elif request.method == 'PUT':
        serializer = NavigationItemSerializer(
            navigation, 
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )    
    if request.method == 'DELETE':
        navigation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
