from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para o admin do Django
    path('catalogo/', include('coderflix.catalogo.urls')),  # Inclui as URLs de catalogo
    path('project/', include('coderflix.project.urls')),    # Inclui as URLs de project
]
