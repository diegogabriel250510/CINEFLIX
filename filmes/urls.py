from django.urls import path, include
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro_filmes"),
    path('home/', views.home, name="home_filmes"),
    path('remover/<int:id>', views.remover, name="remover_filmes")
]
