from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def criar_usuario(request):
    return HttpResponse ("<h1>Bem vindo a página Crud</h1>")
