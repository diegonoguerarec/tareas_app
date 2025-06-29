from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_vista(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        contrasena = request.POST.get('password')

        usuario = authenticate(request=request, username=usuario, password=contrasena)

        if usuario is not None:
            login(request=request, user=usuario)
            return redirect('inicio')
        else:
            error = 'Error el loguear'


    return render(request, 'login.html')

def logout_vista(request):
    logout(request=request)
    return redirect('inicio')
