from django.shortcuts import render

from .forms import ContatoForm
from .forms import ProdutoForm

# Create your views here.
# from django .http import HttpResponse


def index(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')

#view contato
def contato(request):
    form = ContatoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'contato.html', contexto)

def produtos(request):
    contexto = {
        'lista': [
            {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
            {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
            {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
            {'id': 4, 'nome': 'Mouse', 'preco': '40,00'},
            {'id': 5, 'nome': 'Impressora', 'preco': '600,00'},
            {'id': 6, 'nome': 'Scanner', 'preco': '700,00'},
            {'id': 7, 'nome': 'Câmera Web', 'preco': '150,00'},
            {'id': 8, 'nome': 'Headset', 'preco': '120,00'},
            {'id': 9, 'nome': 'Pendrive 32GB', 'preco': '30,00'},
            {'id': 10, 'nome': 'HD Externo 1TB', 'preco': '350,00'},
            {'id': 11, 'nome': 'Estabilizador', 'preco': '200,00'},
            {'id': 12, 'nome': 'Switch 8 portas', 'preco': '180,00'},
            {'id': 13, 'nome': 'Roteador Wi-Fi', 'preco': '220,00'},
        ],
    }
    return render(request, 'produtos/lista.html',contexto)

def form_produto(request):
    form = ProdutoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'produtos/formulario.html', contexto)

def detalhes_produto(request, id):
    contexto = {
        'id': id,
    }
    return render(request, 'produtos/detalhes.html', contexto)

def editar_produto(request, id):
    form = ProdutoForm()
    contexto = {
        'form': form,
    }
    return render(request, 'produtos/formulario.html', contexto)

def excluir_produto(request, id):
    contexto = {
        'id': id,
    }
    return render (request, 'produtos/excluir.html', contexto)

def exibir_item(request, id):
    return render(request,"exibir_item.html", {'id':id})

def perfil(request, usuario):
    return render(request,"perfil.html", {'usuario':usuario})

def diasemana(request, id):
    # Dicionário com os dias da semana
    dia_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado",
    }
    
    # Verifica se o id está no dicionário e retorna o dia correspondente
    dia = dia_semana.get(id, None)
    
    # Verifica se o id é válido
    if dia:
        # Renderiza a página com o dia da semana válido
        return render(request, "diasemana.html", {"dia": dia})
    else:
        # Renderiza uma página de erro ou exibe uma mensagem de dia inválido
        return render(request, "diasemana.html", {"dia": "Dia inválido"})


