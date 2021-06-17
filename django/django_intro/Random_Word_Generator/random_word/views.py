from django.shortcuts import render, redirect 
from django.utils.crypto import get_random_string

def index(request):
    return render(request,"index.html")

def palabra_aleatoria(request):

    request.session['counter'] +=1
    context = {
        "unique_id" : (get_random_string(length=14))
    }

    print(context)
    return render(request,"index.html",context)

def restore(request):
    request.session['counter'] = 0
    return redirect("/")