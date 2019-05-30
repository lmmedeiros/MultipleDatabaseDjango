from django.urls import path, include

from .views import profissao

urlpatterns = [
   path('view/', profissao, name = 'profissao')
]