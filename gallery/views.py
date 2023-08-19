from django.shortcuts import render


def index(request):
    return render(request, 'gallery/index.html')

def imagem(request):
    return render(request, 'gallery/imagem.html')

