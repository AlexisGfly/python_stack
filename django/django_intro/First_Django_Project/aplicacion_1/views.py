from django.shortcuts import render, HttpResponse, redirect

def inicio(request):
    return HttpResponse('Mi Primer Proyecto en Django')

def index(request):
    return HttpResponse('Placeholder para luego mostrar una lista de todos los blogs')

def index2(request):
    return HttpResponse('Placeholder para mostrar un nuevo formulario para crear un nuevo blog')

def create(request):
    return redirect('/')

def show(request,num_1):
    response='Placeholder para mostrar el blog numero: '+str(num_1)
    return HttpResponse(response)

def edit(request,num_1):
    response='Placeholder para editar el blog: '+str(num_1)
    return HttpResponse(response)

def destroy(request,num_1):
    return redirect('/blogs')