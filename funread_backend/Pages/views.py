import datetime
import json
from sre_parse import State
from turtle import title
from wsgiref import headers
from .models import Pages
from .serializers import PageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import hashlib

@api_view(['POST'])
def new_page(request):
    print(request.data)
    data = {
        'pageid': request.data.get('pageid'),
        'bookid': request.data.get('bookid'),
        'elementorder': request.data.get('elementorder'),
        'type': request.data.get('type'),
        'template': request.data.get('template')
    }
    serializer = PageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
