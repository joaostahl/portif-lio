from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Portifólio</h1><p>Bem Vindo a exposição do meu trabalho</p>') 
