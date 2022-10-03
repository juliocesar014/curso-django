from django.urls import path


from . import views


urlpatterns = [
    path("", views.home),  # Página Inicial
    path("receitas/<int:id>/", views.receita),  # Receitas individual

]
