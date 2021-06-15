from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

def inicio1(request):
    context = {
        "date": strftime("%Y-%m-%d", localtime()),
        "time": strftime("%H:%M %p", localtime())
    }
    return render(request,'index.html', context)

def inicio2(request):
    return redirect('/')
