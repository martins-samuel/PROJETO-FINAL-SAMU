from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse ("<h1>Bem vindo a página Crud</h1>")
    #requeste requisição
    #templatehtml entre outros
    #context objetos (python, python com banco de dados)
    return render(request,'marketplace/index.html')

def autentica_membro(request):
    return render(request, 'marketplace/sou_membro.html')
