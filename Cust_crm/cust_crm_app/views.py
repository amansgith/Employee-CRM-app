from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    # check if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate user
        user = authenticate(request=request, username=username, password=password)
        #check if authentication is successful
        if user is not None:
            #login the user
            login(request, user)
            messages.success(request, "✅ you have been logged in!!")
            return redirect('home')
        else:
            messages.error(request, "⚠️ Username or Password is incorrect.")
            return redirect('home')
    else:
        return render(request, 'index.html', {})
    

def logout_user(request):
    logout(request)
    messages.info(request, "You've successfully logged out!")
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})
