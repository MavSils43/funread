
from typing import Any
from django import http
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Per
import json

from django.http.response import JsonResponse
# Create your views here.

class PerView(View):
 @method_decorator(csrf_exempt)
 def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
    
 def get(self,request,id=0):
    if (id>0):
       pers=list(Per.objects.filter(id=id).values())
       if len(pers)>0:
          per=pers[0]
          datos={'message':"Exito",'per': per}
       else:
          datos={'message': "No se han encontrado los personajes..."}
       return JsonResponse(datos)
    else:
      pers = list(Per.objects.values())
      if len(pers) > 0:
        datos={'message':"Exito",'pers': pers}
      else:
        datos={'message': "No se han encontrado los personajes..."}
      return JsonResponse(datos)

 def post(self,request):
    #print(request.body)
    jd=json.loads(request.body)
    #print(jd)
    Per.objects.create(Personaje=jd['Personaje'], Saga=jd['Saga'], Tipo=jd['Tipo'])
    datos={'message':"Exito"}
    return JsonResponse(datos)
        

 def put(self,request,id=0):
    jd=json.loads(request.body)
    pers=list(Per.objects.filter(id=id).values())
    if len(pers) > 0:
       per=Per.objects.get(id=id)
       per.Personaje=jd['Personaje']
       per.Saga=jd['Saga']
       per.Tipo=jd['Tipo']
       per.save()
       datos={'message':"Exito"}
    else:
       datos={'message': "No se han encontrado los personajes..."}
    return JsonResponse(datos)

 def delete(self,request,id=0):
        pers=list(Per.objects.filter(id=id).values())
        if len(pers) > 0:
           Per.objects.filter(id=id).delete()
           datos={'message':"Exito"}
        else:
           datos={'message': "No se han encontrado los personajes..."}
        return JsonResponse(datos)
      