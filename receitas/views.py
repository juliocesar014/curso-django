from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # Return HTTP Response -> Escrever ('html')
    # Return Render -> Renderizar template Html
    return render(request, 'receitas/home.html', context={
        'name': 'Júlio',
        'idade': '20',

    })


def sobre(request):
    return HttpResponse("Sobre")


def contato(request):
    return HttpResponse("Contato")
