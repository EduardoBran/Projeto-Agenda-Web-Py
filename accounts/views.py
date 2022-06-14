from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez o login com sucesso.')
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('login')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    # campo vazio
    if not nome or not sobrenome or not email or not usuario \
            or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/cadastro.html')

    # validando email
    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail inválido.')
        return render(request, 'accounts/cadastro.html')

    # usuario ou senha ter mais que 6 caracteres
    if len(usuario) < 5:
        messages.error(request, 'Usuário precisa ter mais que 6 caracteres.')
        return render(request, 'accounts/cadastro.html')
    if len(senha) < 5:
        messages.error(request, 'Senha precisa ter mais que 6 caracteres.')
        return render(request, 'accounts/cadastro.html')

    # verificando senhas iguais
    if senha != senha2:
        messages.error(request, 'A senha precisa ser igual.')
        return render(request, 'accounts/cadastro.html')

    # verificando para não ter usuario ou email repetidos
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existente.')
        return render(request, 'accounts/cadastro.html')
    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já existente.')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Regitrado com sucesso.')

    user = User.objects.create_user(username=usuario, email=email,
                                    password=senha, first_name=nome,
                                    last_name=sobrenome)
    user.save()
    return redirect('index')


@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
