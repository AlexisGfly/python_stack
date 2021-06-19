from django.shortcuts import render, HttpResponse, redirect

def inicio(request):
    return HttpResponse('marcador de posición para mostrar todas las encuestas creadas')

def nuevo(request):
    return HttpResponse('marcador de posición para que los usuarios agreguen una nueva encuesta')