from django.urls import path 

from .views import index
from .views import list

urlpatterns = [
    path('', index, name='index'),
    path('', list, name='list'),
]
