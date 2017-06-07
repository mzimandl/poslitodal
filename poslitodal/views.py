# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
    
            if user is not None:
                if user.is_active:
                    login(request, user)
	            return redirect('home')
                else:
                    message = 'Zablokovaný účet.'
            else:
                message = 'Špatné jméno nebo heslo. A nebo oboje.'
        return render(request, 'poslitodal/login.html', {'message':message})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'poslitodal/home.html', {'username':request.user})
