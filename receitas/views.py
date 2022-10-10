from django.shortcuts import render
from utils.receitas.factory import make_receita


# from django.http import HttpResponse
# Create your views here.


def home(request):
    # Return HTTP Response -> Escrever ('html')
    # Return Render -> Renderizar template Html
    return render(request, 'receitas/pages/home.html', context={
        'receitas': [make_receita() for _ in range(10)]

    })


def receita(request, id):
    return render(request, 'receitas/pages/receita-view.html', context={
        'receita': make_receita(),
    })
