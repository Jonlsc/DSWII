from django.urls import path
from . import views  # Certifique-se de ter views configuradas para essas URLs

urlpatterns = [
    path('', views.index, name='catalogo_index'),  # Exemplo de URL para o catálogo
]
