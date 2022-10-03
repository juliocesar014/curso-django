from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def home(request):
    # Return HTTP Response -> Escrever ('html')
    # Return Render -> Renderizar template Html
    return render(request, 'receitas/pages/home.html', context={
        'name': 'Júlio',
        'idade': '20',

    })


def receita(request, id):
    return render(request, 'receitas/pages/home.html')
