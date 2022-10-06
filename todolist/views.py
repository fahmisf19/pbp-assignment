from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.models import ToDoList

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolist_items = ToDoList.objects.filter(user=request.user)

    for i in range(len(todolist_items)) :
        if (todolist_items[i].is_finished == True) :
            todolist_items[i].finish = "Finished"
        elif (todolist_items[i].is_finished == False):
            todolist_items[i].finish = "Not finished"
    context = {
        'todolist': todolist_items,
    }
    return render(request, 'todolist.html', context)

def show_create_task(request):
    return render(request, 'create-task.html')

def create_task(request):
    if request.method == "POST":
        x = request.POST.get('title')
        y = request.POST.get('description')
        new_item = ToDoList.objects.create(user=request.user, date = str(datetime.datetime.now().date()), title= x, description = y)
        new_item.save()
        return HttpResponseRedirect('/todolist/')

def finish_task(request, i):
    obj = get_object_or_404(ToDoList, id=i)
    if request.method == 'POST':
        obj.is_finished = not obj.is_finished
        obj.save()
        return redirect('/todolist/')

    return render(request, 'todolist.html', {'obj' : obj})

def delete_task(request, i):
    y = ToDoList.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todolist/') 

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response