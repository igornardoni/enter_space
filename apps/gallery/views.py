from django.shortcuts import render, get_object_or_404, redirect
from apps.gallery.models import Fotografia
from apps.gallery.forms import PhotographForm
from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'gallery/index.html', {"cards": fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'gallery/imagem.html', {"fotografia": fotografia})


def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'gallery/index.html', {"cards": fotografias})


def surpreenda_me(request):
    return render(request, 'gallery/surpreenda_me.html')


def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')
    form = PhotographForm
    if request.method == 'POST':
        form = PhotographForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova imagem cadastrada com sucesso!')
            return redirect('index')
    return render(request, 'gallery/nova_imagem.html', {'form': form})


def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = PhotographForm(instance=fotografia)
    if request.method == 'POST':
        form = PhotographForm(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem editada com sucesso!')
            return redirect('index')
    return render(request, 'gallery/editar_imagem.html', {'form': form, 'foto_id': foto_id})


def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Imagem deletada!')
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True,
                                                                         categoria=categoria)
    return render(request, 'gallery/index.html', {'cards': fotografias})

