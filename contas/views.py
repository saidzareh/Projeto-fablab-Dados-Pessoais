#from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import DadosPessoais
from .forms import DadosPessoaisform


# Create your views here.
def home(request):
    postagens = DadosPessoais.objects.all()
    data={}
    data['postagens'] = postagens

    return render(request, 'contas/home.html', data)

def create(request):
    form = DadosPessoaisform(request.POST or None)
    data = {}
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'contas/create.html', data)

def leitura_postagem(request, pk):
    postagem = DadosPessoais.objects.get(pk=pk)
    data={}
    data['postagem'] = postagem

    return render(request, 'contas/postagem.html', data)

def update(request, pk):
    postagem = DadosPessoais.objects.get(pk=pk)
    form = DadosPessoaisform(request.POST or None, instance=postagem)
    data = {}
    data['postagem'] = postagem
    data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'contas/update.html', data)


def delete(request, pk):
    postagem = DadosPessoais.objects.get(pk=pk)
    postagem.delete()

    return redirect('home')