from django.shortcuts import render
import datetime
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import GorupsCreateSeralizer
from .models import GroupsCreate
from rest_framework import status
import os
import sys
sys.path.append('funread_backend')
import verifyJwt

# Create your views here.

@api_view(['POST'])
def new_group(request):
    
    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    data = {
        'name': request.data.get('name'),
        'idimage': os.path.splitext(request.data.get('image').split('/')[-1])[0],
        'createdby': request.data.get('createdby'),
        'createdat': datetime.datetime.now(),
        'isactive' : 1
    }
    print(data)
    serializer = GorupsCreateSeralizer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listedCreateby(request, createdby):
    # Token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    try:
        createdby = GroupsCreate.objects.filter(createdby=createdby)
    except GroupsCreate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GorupsCreateSeralizer(createdby, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@ api_view(['POST'])
def deletegroup(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    try:
        Groups = GroupsCreate.objects.get(id= request.data.get('idgroup'))
    except GroupsCreate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    Groups.isactive = 0
    Groups.save()
    return Response("group successfully deleted", status=status.HTTP_200_OK)
