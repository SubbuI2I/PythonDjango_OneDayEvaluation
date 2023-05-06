from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
# Create your views here.

# def index(request):
#     return render(request, "ToDoList/index.html")

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/todolist')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)                
                return render(request, 'ToDoList/todolist.html')
            else:
                messages.error(request, "Inavlid User Name or Password")
        return render(request, "ToDoList/login.html")

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def register(request):
    registraion_form = UserRegistrationForm()
    if request.method == 'POST':
        registraion_form = UserRegistrationForm(request.POST)
        if registraion_form.is_valid():
            registraion_form.save()
            messages.success(request, 'Registered Successfuly, Please Login..')
            return redirect('/login')
    return render(request, "ToDoList/register.html", {'registraion_form': registraion_form})


def todolist(request):
    return render(request, "ToDoList/todolist.html")

