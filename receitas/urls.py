from django.urls import path
from receitas.views import home, sobre, contato


urlpatterns = [
    path("", home),  # Página Inicial
    path("sobre/", sobre),  # Sobre
    path("contato/", contato)  # Contato
]
