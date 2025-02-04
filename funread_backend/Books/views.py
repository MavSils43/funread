import datetime
import json
from sre_parse import State
from turtle import title
from wsgiref import headers
from .models import Book
from .serializers import BookSerializer, BookUpdatedBySerializer, bookStateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import hashlib
import sys
sys.path.append('funread_backend')
import verifyJwt

@api_view(['POST'])
def new_book(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    data = {
        'title': request.data.get('title'),
        'category': request.data.get('category'),
        'portrait': request.data.get('portrait'),
        'createdby': request.data.get('createdby'),
        'createdat': datetime.datetime.now(),
        'updatedby': request.data.get('updatedby'),
        'lastupdateat': datetime.datetime.now(),
        'state' : request.data.get('state' ),
        'sharedbook' : request.data.get('sharedbook'),
        'lastupdateby': request.data.get('lastupdateby')
    }
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def bookSearch(request, title):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        print(title)
        book = Book.objects.get(title=title)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def bookChange(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        dataRequest = {
            'title': request.data.get('title'),
        }
        titleSe = dataRequest.get('title')
        book = Book.objects.get(title=titleSe)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    data = {
        'title': request.data.get('new_title'),
        'portrait': request.data.get('portrait'),
        'category': request.data.get('category'),
        'createdby': request.data.get('createdby'),
        'updatedby': request.data.get('updatedby'),
        'lastupdateat': datetime.datetime.now(), 
        'state': request.data.get('state'),
    }
    serializer = BookSerializer(book, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET'])
def listed(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def listed_PublishedBooks(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    book = Book.objects.filter(state=2)
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@ api_view(['GET'])
def listed_NotPublishedBooks(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    book = Book.objects.filter(state=1)
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@ api_view(['GET'])
def listed_PrivateBooks(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    book = Book.objects.filter(state=0)
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def modifyStateToPrivate(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        dataRequest = {
            'title': request.data.get('title'),
        }
        titleSe = dataRequest.get('title')
        book = Book.objects.get(title=titleSe)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {
        'state': 0,
    }
    serializer = bookStateSerializer(book, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def modifyStateToPublish(request):

    #token verification
    authorization_header = request.headers.get('Authorization')
    verify = verifyJwt.JWTValidator(authorization_header)
    es_valido = verify.validar_token()
    if es_valido==False:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        dataRequest = {
            'title': request.data.get('title'),
        }
        titleSe = dataRequest.get('title')
        book = Book.objects.get(title=titleSe)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {
        'state': 2,
    }
    serializer = bookStateSerializer(book, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

