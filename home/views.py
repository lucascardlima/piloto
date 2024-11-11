from django.shortcuts import render

# Create your views here.
# from django .http import HttpResponse


def index(request):
    return render(request, 'index.html')


def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

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


