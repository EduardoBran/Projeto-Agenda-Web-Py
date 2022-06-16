from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.shortcuts import redirect
from django.db.models.functions import Concat
from django.contrib import messages


def inicio(request):
    return render(request, 'contatos/inicio.html')


def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )

    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo não pode ficar vazio.'
        )
        return redirect('index')
    else:
        messages.add_message(
            request,
            messages.SUCCESS,
            'Pesquisa realizada.'
        )

    campos = Concat('nome', Value(' '), 'sobrenome')  # campos existente na bd. Value simula um campo da bd

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    # print(contatos.query)

    paginator = Paginator(contatos, 20)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })