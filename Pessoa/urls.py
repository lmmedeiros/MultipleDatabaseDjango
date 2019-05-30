from django.urls import path, include

from .views import pessoa

urlpatterns = [
   path('view/', pessoa, name = 'pessoa')
]