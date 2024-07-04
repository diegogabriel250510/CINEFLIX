from django.shortcuts import render,redirect
from .models import Filme, Imagem
# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        onde_assistir = request.POST.get('ondeAssistir')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')

        filme = Filme(nome=nome,onde_assistir=onde_assistir,categoria=categoria,descricao=descricao)
        filme.save()
        filmes = Filme.objects.all()    
        return render(request, 'home.html', {'filmes':filmes})

def home(request):
    filmes = Filme.objects.all()    
    return render(request, 'home.html', {'filmes':filmes})

def remover(request, id):
    filme_remover = Filme.objects.filter(id=id)
    if len(filme_remover) == 1:
        filme_remover.delete()
    filmes = Filme.objects.all()
    return render(request, 'home.html', {'filmes':filmes})