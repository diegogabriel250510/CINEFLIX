from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('escolha.urls')),
    path('filmes/', include('filmes.urls')),
    path('series/', include('series.urls')),
]
