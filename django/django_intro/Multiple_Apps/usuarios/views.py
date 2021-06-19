from django.shortcuts import render, HttpResponse, redirect

def inicio(request):
    return HttpResponse('marcador de posición para luego mostrar toda la lista de usuarios')

def nuevo(request):
    return HttpResponse('Aplicación de Usuarios')

def log(request):
    return HttpResponse('marcador de posición para que los usuarios inicien sesión')

def reg(request):
    return HttpResponse('marcador de posición para que los usuarios creen un nuevo registro de usuario')
