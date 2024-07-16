from django.shortcuts import render
from .models import Genero, Usuario, Anime,Marca,Figura
from .forms import GeneroForm,UsuarioForm,AnimeForm,MarcaForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context={
        "usuario": "",
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

@login_required
def crud(request):
    usuarios = Usuario.objects.all()
    context = {
        "usuarios": usuarios,
    }
    return render(request, "pages/crud.html", context)


def user_add(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {
            "generos": generos,
        }
        return render(request, "pages/user_add.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fechaNac = request.POST["fecha"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]
        activo = True

        objGenero = Genero.objects.get(id_genero=genero)

        obj = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            telefono=telefono,
            email=correo,
            password=password,
            direccion=direccion,
            activo=activo,
        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/user_add.html", context)


def user_del(request, pk):
    try:
        usuario = Usuario.objects.get(rut=pk)
        usuario.delete()

        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Registro Eliminado",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Error,Rut no encontrado...",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)

def user_findEdit(request,pk):
    if pk!="":
        """ 
            objects.get() = Obtener datos con filtro
            objects.all() = Obtener todos
        """
        usuario = Usuario.objects.get(rut=pk)
        generos = Genero.objects.all()

        context={
            "usuario":usuario,
            "generos":generos,
        }
        return render(request,"pages/user_update.html",context)
    else:
        usuarios = Usuario.objects.all()
        context={
            "mensaje":"Error,Rut no encontrado",
            "usuarios":usuarios
        }
        return render(request,"pages/crud.html",context)

def user_update(request):
    if request.method=="POST":
        """ 
            Capturo todos los datos del front
            Identificamos
            Asignamos nombre 
        """
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fechaNac = request.POST["fecha"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]
        activo = True

        """ Obtengo genero desde la BDD para modificar """
        objGenero = Genero.objects.get(id_genero=genero)

        """ Genero la instancia """

        obj = Usuario(
            rut=rut,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            telefono=telefono,
            email=correo,
            password=password,
            direccion=direccion,
            activo=activo,
        )
        obj.save()

        generos = Genero.objects.all()
        context = {
            "mensaje": "Modificado con Exito",
            "generos":generos,
            "usuario":obj,
        }
        return render(request, "pages/user_update.html", context)
    
@login_required
def crud_figura(request):
    usuarios = Usuario.objects.all()
    context = {
        "usuarios": usuarios,
    }
    return render(request, "pages/crud.html", context)


def figura_add(request):
    if request.method != "POST":
        figuras = Figura.objects.all()
        context = {
            "figuras": figuras,
        }
        return render(request, "pages/figura_add.html", context)
    else:
        id_figura = request.POST["idfigura"]
        nombre_figura = request.POST["nombre"]
        anime = request.POST["anime"]
        marca = request.POST["marca"]
        fecha_lanzamiento = request.POST["fecha"]
        precio = request.POST["precio"]
        tamano = request.POST["tamano"]


        objAnime = Anime.objects.get(id_anime=anime)
        objMarca= Marca.objects.get(id_marca=marca)

        obj = Usuario.objects.create(
            rut=id_figura,
            nombre=nombre_figura,
            anime=objAnime,
            marca=objMarca,
            fecha_lanzamiento=fecha_lanzamiento,
            precio=precio,
            tamano=tamano,
 
        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/figura_add.html", context)


def figura_del(request, pk):
    try:
        figura = Figura.objects.get(id_figura=pk)
        figura.delete()

        figuras = Figura.objects.all()
        context = {
            "mensaje": "Figura Eliminada",
            "figuras": figuras,
        }
        return render(request, "pages/crud_figura.html", context)
    except:
        figuras = Figura.objects.all()
        context = {
            "mensaje": "Error,Id_Figura no encontrado...",
            "figuras": figuras,
        }
        return render(request, "pages/crud_figura.html", context)

def figura_findEdit(request,pk):
    if pk!="":
        """ 
            objects.get() = Obtener datos con filtro
            objects.all() = Obtener todos
        """
        figura = Figura.objects.get(id_figura=pk)
        marcas = Marca.objects.all()
        animes = Anime.objects.all()

        context={
            "figura":figura,
            "marcas":marcas,
            "animes":animes,

        }
        return render(request,"pages/figura_update.html",context)
    else:
        figuras = Figura.objects.all()
        context={
            "mensaje":"Error,Rut no encontrado",
            "figuras":figuras
        }
        return render(request,"pages/crud_figura.html",context)

def figura_update(request):
    if request.method=="POST":
        """ 
            Capturo todos los datos del front
            Identificamos
            Asignamos nombre 
        """
        id_figura = request.POST["idfigura"]
        nombre_figura = request.POST["nombre"]
        anime = request.POST["anime"]
        marca = request.POST["marca"]
        fecha_lanzamiento = request.POST["fecha"]
        precio = request.POST["precio"]
        tamano = request.POST["tamano"]


        objAnime = Anime.objects.get(id_anime=anime)
        objMarca= Marca.objects.get(id_marca=marca)

        obj = Usuario.objects.create(
            rut=id_figura,
            nombre=nombre_figura,
            anime=objAnime,
            marca=objMarca,
            fecha_lanzamiento=fecha_lanzamiento,
            precio=precio,
            tamano=tamano,
 
        )
        obj.save()

        animes = Anime.objects.all()
        marcas = Marca.objects.all()

        context = {
            "mensaje": "Modificado con Exito",
            "animes":animes,
            "marcas":marcas,

            "figura":obj,
        }
        return render(request, "pages/figura_update.html", context)
    


@login_required
def crud_genero(request):
    generos = Genero.objects.all()

    context={
        "generos":generos,
    }
    return render(request,"pages/crud_genero.html",context)

def genero_add(request):
    formGenero = GeneroForm()
    formUsuario = UsuarioForm()
    if request.method=="POST":
        nuevo = GeneroForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":formGenero
            }
            return render(request,"pages/genero_add.html",context)
    else:
        context = {
            "form":formGenero,
            "form2":formUsuario
        }
        return render(request,"pages/genero_add.html",context)

def genero_del(request,pk):
    try:
        genero = Genero.objects.get(id_genero=pk)
        genero.delete()

        generos = Genero.objects.all()
        context={
            "mensaje":"Registro eliminado exitosamente",
            "generos":generos
        }
        return render(request,"pages/crud_genero.html",context)
    except:
        generos = Genero.objects.all()
        context={
            "mensaje":"Error, Genero no encontrado...",
            "generos":generos
        }
        return render(request,"pages/crud_genero.html",context)

def genero_edit(request,pk):
    if pk!="":
        genero = Genero.objects.get(id_genero=pk)
        form = GeneroForm(instance=genero)
        if request.method=="POST":
            nuevo = GeneroForm(request.POST,instance=genero)

            if nuevo.is_valid():
                nuevo.save()

                context ={
                    "mensaje":"Modificado con exito",
                    "form":nuevo
                }
                return render(request,"pages/genero_edit.html",context)
        else:
            context={
                "form":form,
            }
            return render(request,"pages/genero_edit.html",context)
    else:
        generos = Genero.objects.all()
        context={
            "mensaje":"Error, genero no encontrado",
            "generos":generos
        }
        return render(request,"pages/crud_genero.html",context)
@login_required
def crud_anime(request):
    animes = Anime.objects.all()

    context={
        "animes":animes,
    }
    return render(request,"pages/crud_anime.html",context)

def anime_add(request):
    formAnime = AnimeForm()
    formUsuario = UsuarioForm()
    if request.method=="POST":
        nuevo = AnimeForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":formAnime
            }
            return render(request,"pages/anime_add.html",context)
    else:
        context = {
            "form":formAnime,
            "form2":formUsuario
        }
        return render(request,"pages/anime_add.html",context)

def anime_del(request,pk):
    try:
        anime = Anime.objects.get(id_anime=pk)
        anime.delete()

        animes = Anime.objects.all()
        context={
            "mensaje":"Registro eliminado exitosamente",
            "animes":animes
        }
        return render(request,"pages/crud_anime.html",context)
    except:
        animes = Anime.objects.all()
        context={
            "mensaje":"Error, Anime no encontrado...",
            "animes":animes
        }
        return render(request,"pages/crud_anime.html",context)

def anime_edit(request,pk):
    if pk!="":
        anime = Anime.objects.get(id_anime=pk)
        form = AnimeForm(instance=anime)
        if request.method=="POST":
            nuevo = AnimeForm(request.POST,instance=anime)

            if nuevo.is_valid():
                nuevo.save()

                context ={
                    "mensaje":"Modificado con exito",
                    "form":nuevo
                }
                return render(request,"pages/anime_edit.html",context)
        else:
            context={
                "form":form,
            }
            return render(request,"pages/anime_edit.html",context)
    else:
        animes = Anime.objects.all()
        context={
            "mensaje":"Error, anime no encontrado",
            "animes":animes
        }
        return render(request,"pages/crud_anime.html",context)

@login_required
def crud_marca(request):
    marcas = Marca.objects.all()

    context={
        "marcas":marcas,
    }
    return render(request,"pages/crud_marca.html",context)

def marca_add(request):
    formMarca = MarcaForm()
    formUsuario = UsuarioForm()
    if request.method=="POST":
        nuevo = MarcaForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":formMarca
            }
            return render(request,"pages/marca_add.html",context)
    else:
        context = {
            "form":formMarca,
            "form2":formUsuario
        }
        return render(request,"pages/marca_add.html",context)

def marca_del(request,pk):
    try:
        marca = Marca.objects.get(id_marca=pk)
        marca.delete()

        marcas = Marca.objects.all()
        context={
            "mensaje":"Registro eliminado exitosamente",
            "marcas":marcas
        }
        return render(request,"pages/crud_marca.html",context)
    except:
        marcas = Marca.objects.all()
        context={
            "mensaje":"Error, Marca no encontrado...",
            "marcas":marcas
        }
        return render(request,"pages/crud_marca.html",context)

def marca_edit(request,pk):
    if pk!="":
        marca = Marca.objects.get(id_marca=pk)
        form = MarcaForm(instance=marca)
        if request.method=="POST":
            nuevo = MarcaForm(request.POST,instance=marca)

            if nuevo.is_valid():
                nuevo.save()

                context ={
                    "mensaje":"Modificado con exito",
                    "form":nuevo
                }
                return render(request,"pages/marca_edit.html",context)
        else:
            context={
                "form":form,
            }
            return render(request,"pages/marca_edit.html",context)
    else:
        marcas = Marca.objects.all()
        context={
            "mensaje":"Error, marca no encontrado",
            "marcas":marcas
        }
        return render(request,"pages/crud_marca.html",context)

def loginSession(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username=="j.riquelmee" and password=="pass1234":
            request.session["user"] = username
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/crud.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
                "design":"alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"pages/login.html",context)
    else:
        context = {

        }
        return render(request,"pages/login.html",context)

def conectar(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/crud.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
                "design":"alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"pages/login.html",context)
    else:
        context = {

        }
        return render(request,"pages/login.html",context)

def desconectar(request):   
    if request.user.is_authenticated:
        logout(request)
    
    context = {
        "mensaje":"Desconectado con exito",
        "design":"alert alert-success w-50 mx-auto text-center",
    }
    return render(request,"pages/login.html",context)
