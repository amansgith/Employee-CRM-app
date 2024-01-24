from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def index(request):
    records = Record.objects.all()

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
    # this means that the user is already logged in..
    else:
        return render(request, 'index.html', {'records':records})
    

def logout_user(request):
    logout(request)
    messages.info(request, "You've successfully logged out!")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Account created for {username}! You are now logged in!!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})


def user_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.warning(request, "Please Login to view your record.")
        return redirect('home')
    

def del_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record has been deleted successfully!!")
        return redirect('home')
    else:
        messages.warning(request, "Please Login to do that!!")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_record.html',{'form': form})
    else:
        messages.success(request,"You are not Logged In")
        return redirect('home')
    

def edit_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!!")
            return redirect('home')
        return render(request,'edit_record.html',{"form" : form })
    else:
        messages.error(request, "Please login first to access this feature!")
        return redirect("home")