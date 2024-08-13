from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    error = None
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('dashboard')
        else :
            error = 'Usuario o comtraseña incorrectos '
            return render(request, 'login.html', {'error':error})
    return render(request,'login.html')


def dashboard(request):
    return render(request, 'dashboard.html' )