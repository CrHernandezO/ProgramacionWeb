from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        "usuario": "Cristobal Hernandez",
    }
    return render(request,"pages/index.html",context)


def catalogo(request):

    context={}
    return render(request,"pages/catalogo.html",context)

def iniciosesion(request):

    context={}
    return render(request,"pages/iniciosesion.html",context)

def registro(request):

    context={}
    return render(request,"pages/registro.html",context)

def kaoricompra(request):

    context={}
    return render(request,"pages/kaoricompra.html",context)

def preguntasF(request):

    context={}
    return render(request,"pages/preguntasF.html",context)

def somos(request):

    context={}
    return render(request,"pages/somos.html",context)
def crud(request):
    context={}
    return render(request,"pages/pages/crud.html",context)
def user_add(request):
    context={}
    return render(request,"pages/pages/user_add.html",context)
def crud_genero(request):
    context={}
    return render(request,"pages/pages/crud_genero.html",context)
def genero_add(request):
    context={}
    return render(request,"pages/pages/genero_add.html",context)