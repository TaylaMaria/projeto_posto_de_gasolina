from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'core/home.html', {
        'titulo': 'Posto de Gasolina - Seu Combustível com Qualidade'})

def sobre(request):
    return render(request,'core/sobre.html', {'titulo:': 'Sobre Nós'})


    

