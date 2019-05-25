from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    return render(request, 'index.html')

def home(request):

    now = datetime.datetime.now()

    clock={'now':now}


    return render(request, 'index.html',clock)