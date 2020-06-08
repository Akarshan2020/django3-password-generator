from django.shortcuts import render
from django.http import HttpResponse            #imports the HttpResponse
import random
# Create your views here.
"""def home(request):
    return HttpResponse('Hi! There')            #returns the output on the screen"""

def home(request):
        return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):
    chars=list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))

    if request.GET.get('specialchar'):
        chars.extend(list('.,/?><!@#$%&*^{}[]()'))

    length=int(request.GET.get('length',12))            #here 12 is a default value
    thepassword=" "

    for x in range(length):
        thepassword+=random.choice(chars)
    return render(request,'generator/password.html', {'password': thepassword})
