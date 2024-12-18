# coderflix/project/urls.py
from django.urls import path
from catalogo import views  # Corrigido para importar views de catalogo

urlpatterns = [
    path('', views.index, name='index'),  # A view 'index' de catalogo
]
