from django.shortcuts import render

def index(request):
    return render(request, 'catalogo/index.html')  # Assumindo que você tenha um template index.html
