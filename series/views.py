from django.shortcuts import render
from .models import Serie
# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro_series.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        onde_assistir = request.POST.get('ondeAssistir')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        temporadas = request.POST.get('temporadas')
        episodios = request.POST.get('episodios')

        serie = Serie(nome=nome,onde_assistir=onde_assistir,categoria=categoria,descricao=descricao,temporadas=temporadas,episodios=episodios)
        serie.save()
        series = Serie.objects.all()
        return render(request, 'home_series.html', {'series':series})

def home(request):
    series = Serie.objects.all()
    return render(request, 'home_series.html', {'series':series})
def remover(request, id):
    serie_remover = Serie.objects.filter(id=id)
    if len(serie_remover) == 1:
        serie_remover.delete()
    series = Serie.objects.all()
    return render(request, 'home_series.html', {'series':series})   