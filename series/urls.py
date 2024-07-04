from django.urls import path, include
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro_series"),
    path('home/', views.home, name="home_series"),
    path('remover/<int:id>', views.remover, name="remover_series")
]
