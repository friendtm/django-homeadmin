from django.shortcuts import render, redirect
from . models import Task, NewUser, Produto
from . forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Homepage
@login_required(login_url='/login')
def home(request):
    tasks = Task.objects.all()
    prod = Produto.objects.all()
    dic = {
        'tasks': tasks,
        'prods': prod,
    }
    return render(request, 'homeapp/index.html', dic)


# Criar Tarefa
def create_task(request):
    user = request.user
    
    if request.method == "POST":
        task_name = request.POST.get("task-name")
        task = Task.objects.create(tname=task_name, user=user)
        task.save()
        messages.success(request, "Tarefa criada!")
        return redirect('home')
    
    return render(request, 'homeapp/index.html')


# Apagar Tarefa
def delete_task(request, id):
    delete_task = Task.objects.filter(id=id)
    delete_task.delete()
    messages.success(request, "Tarefa apagada!")
    
    return redirect(home)


# Adicionar Produto à Lista de Compras
def create_prod(request):
    user = request.user
    
    if request.method == "POST":
        prod_name = request.POST.get("prod-name")
        prod = Produto.objects.create(pname=prod_name, user=user)
        prod.save()
        messages.success(request, "Produto adicionado à Lista!")
        return redirect('home')
    
    return render(request, 'homeapp/index.html')


# Remover Produto da Lista de Compras
def delete_prod(request, id):
    delete_prod = Produto.objects.filter(id=id)
    delete_prod.delete()
    messages.success(request, "Produto removido da Lista!")
    
    return redirect(home)


# Registar Utilizador
def register_user(request):
    if request.user.is_authenticated:
        return redirect(home)
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            fname = form.cleaned_data.get("fname")
            password = form.cleaned_data.get("password1")
            form.save()
            new_user = authenticate(username=username, password=password)
                
            if new_user is not None:
                login(request, new_user)
                messages.success(request, "Conta criada com sucesso!")
                return redirect(home)
            
    form = SignUpForm()   
    context = {'form':form, 'messages':messages}
    return render(request, 'homeapp/register.html', context)