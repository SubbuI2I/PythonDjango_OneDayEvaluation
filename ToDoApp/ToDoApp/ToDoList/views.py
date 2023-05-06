from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, ToDoListForm, ToDoItemForm
from .models import ToDoList, ToDoItem
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def todo_item(request, todolist_id):
    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        # breakpoint()
        if form.is_valid():
            print('form valid')
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            todolist = ToDoList.objects.get_or_create(id=todolist_id)
            due_date = form.cleaned_data['due_date']
            # created_at = form.cleaned_data['created_at']
            is_completed = form.cleaned_data['is_completed']
            item = ToDoItem(title = title, description=description, due_date= due_date,  is_completed = is_completed)
            item.save()
            messages.success(request, 'Item added succesfully !')
            items = ToDoItem.objects.all()
            context = {
                'items' : items,
                'todolist_id': todolist_id
            }
            return render(request, "ToDoList/todo-items.html" , context)
        else:
            messages.error(request, 'Invalid form, please check and update')
        return render(request, "ToDoList/todo-items.html")
    else:
        items = ToDoItem.objects.all()
        form = ToDoItemForm()
        context = {
            'form': form,
            'items': items,
            'todolist_id': todolist_id
        } 
        return render(request, "ToDoList/todo-items.html", context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/todo-list')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)                
                return render(request, 'ToDoList/todo-list.html')
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


def todo_list(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ToDoListForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']

                list_obj = ToDoList(
                    title=title, description=description, uploaded_by = request.user.username )
                list_obj.save()
                messages.success(request, 'List Created Successfully !!')
                return redirect('/')
    return render(request, "ToDoList/todo-list.html")

