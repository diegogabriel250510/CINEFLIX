from django.shortcuts import render

# Create your views here.
def escolha(request):
    return render(request, "escolha.html")