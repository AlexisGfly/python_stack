from django.shortcuts import render, redirect 
from django.utils.crypto import get_random_string
import random
from time import gmtime, strftime, localtime

def index(request):
    return render(request,"index.html")

def casino_1(request):
    request.session['valor_1'] = random.randint(10, 20)
    request.session['valor_2'] = 0
    request.session['valor_3'] = 0
    request.session['valor_4'] = 0

    val_1 = request.session['valor_1']

    request.session['date'] = strftime("(%Y/%m/%d %H:%M:%S %p)", localtime())
    request.session['historial'] = 'Earned',val_1,'goals from the farm!'

    msg = (request.session['historial'] , request.session['date'])

    (request.session['messages']).append(msg)

    print('Earned',val_1,'goals from the farm!')
    return redirect("/process_money")

def casino_2(request):
    request.session['valor_1'] = 0
    request.session['valor_2'] = random.randint(5, 10)
    request.session['valor_3'] = 0
    request.session['valor_4'] = 0

    val_2 = request.session['valor_2']

    request.session['date'] = strftime("(%Y/%m/%d %H:%M:%S %p)", localtime())
    request.session['historial'] = 'Earned',val_2,'goals from the cave!'

    msg = (request.session['historial'] , request.session['date'])

    (request.session['messages']).append(msg)

    print('Earned',val_2,'goals from the cave!')
    return redirect("/process_money")

def casino_3(request):
    request.session['valor_1'] = 0
    request.session['valor_2'] = 0
    request.session['valor_3'] = random.randint(2, 5)
    request.session['valor_4'] = 0

    val_3 = request.session['valor_3']

    request.session['date'] = strftime("(%Y/%m/%d %H:%M:%S %p)", localtime())
    request.session['historial'] = 'Earned',val_3,'goals from the house!'

    msg = (request.session['historial'] , request.session['date'])

    (request.session['messages']).append(msg)

    print('Earned',val_3,'goals from the house!')
    return redirect("/process_money")

def casino_4(request):
    request.session['valor_1'] = 0
    request.session['valor_2'] = 0
    request.session['valor_3'] = 0
    request.session['valor_4'] = random.randint(-50, 50)

    val_4 = request.session['valor_4']

    request.session['date'] = strftime("(%Y/%m/%d %H:%M:%S %p)", localtime())

    if val_4 > 0:
        print('Earned',val_4,'goals from the casino!')
        request.session['historial'] = 'Earned',val_4,'goals from the casino!'
        
        msg = (request.session['historial'] , request.session['date'])

        (request.session['messages']).append(msg)

    else:
        print('Entered a casino and lost',abs(val_4),'goals... Ouch..')
        request.session['historial'] = 'Entered a casino and lost',abs(val_4),'goals... Ouch..'
        
        msg = (request.session['historial'] , request.session['date'])

        (request.session['messages']).append(msg)

    return redirect("/process_money")

def procesa_oro(request):
    val_1 = request.session['valor_1']
    val_2 = request.session['valor_2']
    val_3 = request.session['valor_3']
    val_4 = request.session['valor_4']

    val_ant = request.session['total']

    request.session['total'] = val_ant + val_1 + val_2 + val_3 + val_4

    if request.session['total'] < 0:
        print ("Game Over...! =(")
        return redirect("/reset")
    return redirect("/")

def restore(request):
    if request.session['total'] < 0:
        request.session['date'] = strftime("(%Y/%m/%d %H:%M:%S %p)", localtime())
        request.session['historial'] = 'Game Over...! =('

        msg = (request.session['historial'] , request.session['date'])

        (request.session['messages']).append(msg)

        request.session['valor_1'] = 0
        request.session['valor_2'] = 0
        request.session['valor_3'] = 0
        request.session['valor_4'] = 0
        request.session['total'] = 0
        return redirect("/")
        
    request.session['valor_1'] = 0
    request.session['valor_2'] = 0
    request.session['valor_3'] = 0
    request.session['valor_4'] = 0
    request.session['total'] = 0

    request.session['date'] = '...'
    request.session['historial'] = 'Resultados'

    request.session['messages'] = []

    return redirect("/")