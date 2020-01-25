from django.shortcuts import render
from django.http import HttpResponse

from .models import Dog

def index(request):
    return HttpResponse("Hello world!")

def about(request):
    return HttpResponse("To jest testowa strona.")

def cool_text(request, ile_gwiazdek, user_text):
    text = '*' * ile_gwiazdek + user_text.upper() + '*' * ile_gwiazdek
    return HttpResponse(text)

def hello(request, imie):
    return render(request, 'examples/hello.html',
                  {'imie': imie})

def calculator(request, dzialanie, a, b):
    if dzialanie == 'add':
        result = a + b
    elif dzialanie == 'sub':
        result = a - b
    elif dzialanie == 'mul':
        result = a * b
    elif dzialanie == 'div':
        if b == 0:
            result = "Dzielenie przez zero!"
        else:
            result = a / b
    else:
        result = "Nieznane działanie"

    return HttpResponse(result)

def dogs(request):
    dog_list = Dog.objects.all()
    # return HttpResponse(", ".join(str(d) for d in dog_list))
    return render(request, 'examples/dogs.html',
        {'dogs': dog_list})

def dog(request, id):
    dog = Dog.objects.get(id=id)
    return render(request, 'examples/dog.html',
                  {'dog': dog})