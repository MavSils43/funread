from django.urls import path
from .views import PerView

urlpatterns = [
   path('pers/',PerView.as_view(),name='Per_list'),
   path('pers/<int:id>',PerView.as_view(),name='Per_process')
]