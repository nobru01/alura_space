from django.shortcuts import render
# from django.http import HttpResponse

def index(request):

    dados={
        1: {
            'nome':'Nome_foto_1',
            'legenda':'Fonte_1'
        },
        2: {
            'nome':'Nome_foto_2',
            'legenda':'Fonte_2'
        },
    }
    return render(request, 'galeria/index.html',{'cards':dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')