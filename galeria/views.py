from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from galeria.models import Fotografia

def index(request):

        # ordena pela data da fotografia decrescente Maior para menor data
    fotografia=Fotografia.objects. \
        order_by("-data_fotografia").filter(publicada=True)

    return render(request, 'galeria/index.html',{'cards':fotografia})

def imagem(request,foto_id):

    # 1º - Tudo começou com a montagem do caminho no index.html passando tbm um parâmetro id na url
    # 2º - Captura do parâmetro id na url /<int:foto_id> (alteração do urls.py)
    # 3º - Inserção do parâmetro adicional da função da views -> retorno do objeto para a imagem.html


    fotografia=get_object_or_404(Fotografia,pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia':fotografia})

def buscar(request):

    fotografia=Fotografia.objects. \
        order_by("-data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar=request.GET['buscar']
        if nome_a_buscar:
            fotografia=fotografia.filter(nome__icontains=nome_a_buscar)


    return render(request,'galeria/buscar.html',{'cards':fotografia})