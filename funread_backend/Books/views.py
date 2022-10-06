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

@api_view(['POST'])
def new_book(request):
    data = {
        'title': request.data.get('title'),
        'category': request.data.get('category'),
        'portrait': request.data.get('lastname'),
        'createdby_id': request.data.get('createdBy'),
        'createdAt': datetime.datetime.now(),
        'updatedby_id': request.data.get('updatedBy'),
        'updatedAt': datetime.datetime.now(),
        'state' : request.data.get('state' ),
        'sharedBook' : request.data.get('sharedBook'),
    }
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def bookSearch(request, bookid):
    try:
        book = Book.objects.get(bookid=bookid)
        print(book)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def bookChange(request):
    try:
        dataRequest = {
            'title': request.data.get('title'),
        }
        titleSe = dataRequest.get('title')
        book = Book.objects.get(title=titleSe)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = {
        'tile': request.data.get('title'),
        'portrait': request.data.get('portrait'),
        'category': request.data.get('category'),
        'updatedBy': request.data.get('updatedBy'),
        'updatedAt': request.data.get('updatedAt'), 
    }
    serializer = BookSerializer(book, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET'])
def listed(request):
    user = Book.objects.all()
    serializer = BookSerializer(user, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def listed_PublishedBooks(request):
    book = Book.objects.filter(state=2)
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@ api_view(['GET'])
def listed_NotPublishedBooks(request):
    book = Book.objects.filter(state=1)
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@ api_view(['GET'])
def listed_PrivateBooks(request):
    book = Book.objects.filter(state=0)
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def modifyStateToPrivate(request):
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
