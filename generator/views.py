from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, template_name='generator/home.html')

def about(request):
    return render(request, template_name='generator/about.html')

def password(request):
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    characters = list('abcdefghijklmnopqrstuvwxyz')
    numbers = list('1234567890')
    special = "!@#$%^&*()_+"
    length = int(request.GET.get('length'))
    # thepassword = ''
    if request.GET.get('uppercase'):
        characters.extend(uppercase)
    if request.GET.get('numbers'):
        characters.extend(numbers)
    if request.GET.get('special'):
        characters.extend(special)
    thepassword = ''.join([random.choice(characters) for _ in range(length)])
    return render(request, 'generator/password.html', {'passwordtest':thepassword})
