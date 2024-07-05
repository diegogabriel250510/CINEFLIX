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
def alterar(request, id):
    if request.method == "GET":
        filmes = Filme.objects.filter(id=id)
        return render(request, 'alterar_filmes.html', {'filmes':filmes})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        onde_assistir = request.POST.get('onde_assistir')
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        

        filme_editada = Filme(nome=nome,
                              onde_assistir=onde_assistir,
                              categoria=categoria,
                              descricao=descricao)
        filme_editada.save()

        filmes = Filme.objects.all()
        return render(request, 'home.html', {'filmes':filmes})