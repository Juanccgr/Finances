from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponse

# Create your views here.


@login_required
def index(request):
    return render (request,'test1/base.html')

def exit(request):
    logout(request)
    return redirect('/')

