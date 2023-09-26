from django.shortcuts import render, redirect
from users.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(request, username=nome, password=senha)

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome}, logado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar login!')
                return redirect('login')

    return render(request, 'users/login.html', {"form": form})

def cadastro(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            if form['senha'].value() != form['confirmar_senha'].value():
                messages.error(request, 'As senhas não são iguais!')
                return redirect('cadastro')

            nome = form['nome_completo'].value()
            email = form['email'].value()
            senha = form['senha'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existe!')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            usuario.save()
            messages.success(request, 'Cadastro efetuado com  sucesso!')
            return redirect('login')

    return render(request, 'users/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')
