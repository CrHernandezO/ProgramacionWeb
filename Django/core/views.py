from django.shortcuts import render, redirect, get_object_or_404
from .models import Rol, Usuario, Anime,Marca,Figura,CarritoItem
from .forms import RolForm,UsuarioForm,AnimeForm,MarcaForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import check_password

# Create your views here.
def index(request):
    context={
        "usuario": "",
    }
    return render(request,"pages/index.html",context)

def registro_usuario(request):
    if request.method != "POST":
            rols = Rol.objects.all()
            context = {
                "rols": rols,
            }
            return render(request, "pages/user_add.html", context)
    else:
        username = request.POST["username"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        rol = request.POST["rol"]
        telefono = request.POST["telefono"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]

        objRol = Rol.objects.get(id_rol=rol)

        obj = Usuario.objects.create(
            email=username,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            id_rol=objRol,
            telefono=telefono,
            password=password,
            direccion=direccion,
        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/index.html", context)

    # Si es GET o si hay algún error, renderiza el formulario de registro
    rols = Rol.objects.all()
    context = {
        'rols': rols,
    }
    return render(request, 'pages/registro.html', context)




def catalogo(request):
    figuras = Figura.objects.all()
    context = {
        'figuras': figuras,
    }
    return render(request, 'pages/catalogo.html',context)


@login_required
def agregar_al_carrito(request, figura_id):
    figura = get_object_or_404(Figura, id_figura=figura_id)
    usuario = request.user  # Obtener el usuario autenticado actualmente
    print(f"Usuario encontrado: {usuario}")  # Para debugging: verifica si el usuario se encuentra correctamente

    # No necesitas buscar el usuario de nuevo si ya está autenticado
    carrito_item, created = CarritoItem.objects.get_or_create(user=usuario, figura=figura)
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    
    return redirect('carrito')

@login_required
def restar_del_carrito(request, item_id):
    carrito_item = get_object_or_404(CarritoItem, id=item_id)
    if carrito_item.cantidad > 1:
        carrito_item.cantidad -= 1
        carrito_item.save()
    else:
        carrito_item.delete()  # Elimina el item si la cantidad es 1
    return redirect('carrito')
@login_required
def eliminar_del_carrito(request, item_id):
    carrito_item = get_object_or_404(CarritoItem, id=item_id)
    carrito_item.delete()
    return redirect('carrito')

@login_required
def carrito(request):
    usuario = get_object_or_404(Usuario, email=request.user.username)
    carrito_items = CarritoItem.objects.filter(user=usuario)
    
    # Calcular el subtotal para cada item del carrito
    for item in carrito_items:
        item.subtotal = item.figura.precio * item.cantidad
    
    total = sum(item.subtotal for item in carrito_items)
    
    context = {
        'carrito_items': carrito_items,
        'total': total,
    }
    return render(request, 'base/carrito.html', context)

def iniciocliente(request):
    if request.method == 'POST':
        username = request.POST.get('correo')
        password = request.POST.get('pass')

        try:
            usuario = Usuario.objects.get(email=username)

            # Verificar la contraseña (aquí debes implementar tu lógica de autenticación)
            if password == usuario.password:  # Ejemplo básico, deberías usar hash y verificación segura
                # Autenticación exitosa, redirigir o realizar alguna acción
                # Por ejemplo, puedes redirigir a la página de perfil del usuario
                return redirect('perfil_cliente')  # Reemplaza 'perfil_cliente' por la URL correspondiente

            else:
                # Contraseña incorrecta
                messages.error(request, 'Contraseña incorrecta. Inténtelo de nuevo.')

        except Usuario.DoesNotExist:
            # Usuario no encontrado
            messages.error(request, 'Usuario con RUT especificado no encontrado.')

    return render(request, 'pages/iniciocliente.html')

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

@login_required
def user_add(request):
    if request.method != "POST":
        rols = Rol.objects.all()
        context = {
            "rols": rols,
        }
        return render(request, "pages/user_add.html", context)
    else:
        username = request.POST["username"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        rol = request.POST["rol"]
        telefono = request.POST["telefono"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]

        objRol = Rol.objects.get(id_rol=rol)

        obj = Usuario.objects.create(
            email=username,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            id_rol=objRol,
            password=password,
            telefono=telefono,
            direccion=direccion,
        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/user_add.html", context)

@login_required
def user_del(request, pk):
    try:
        usuario = Usuario.objects.get(correo=pk)
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
@login_required
def user_findEdit(request,pk):
    if pk!="":
        """ 
            objects.get() = Obtener datos con filtro
            objects.all() = Obtener todos
        """
        usuario = Usuario.objects.get(email=pk)
        rols = Rol.objects.all()

        context={
            "usuario":usuario,
            "rols":rols,
        }
        return render(request,"pages/user_update.html",context)
    else:
        usuarios = Usuario.objects.all()
        context={
            "mensaje":"Error,Rut no encontrado",
            "usuarios":usuarios
        }
        return render(request,"pages/crud.html",context)
@login_required
def user_update(request):
    if request.method=="POST":
        """ 
            Capturo todos los datos del front
            Identificamos
            Asignamos nombre 
        """
        username = request.POST["username"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        rol = request.POST["rol"]
        telefono = request.POST["telefono"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]

        """ Obtengo rol desde la BDD para modificar """
        objRol = Rol.objects.get(id_rol=rol)

        """ Rol la instancia """

        obj = Usuario(
            email=username,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            id_rol=objRol,
            telefono=telefono,
            password=password,
            direccion=direccion,
        )
        obj.save()

        rols = Rol.objects.all()
        context = {
            "mensaje": "Modificado con Exito",
            "rols":rols,
            "usuario":obj,
        }
        return render(request, "pages/user_update.html", context)
    
@login_required
def crud_figura(request):
    figuras = Figura.objects.all()
    context = {
        "figuras": figuras,
    }
    return render(request, "pages/crud_figura.html", context)

@login_required

def figura_add(request):
    if request.method != "POST":
        animes = Anime.objects.all()
        marcas = Marca.objects.all()

        context = {
            "animes": animes,
            "marcas": marcas,
        }
        return render(request, "pages/figura_add.html", context)
    else:
        nombre_figura = request.POST["nombre"]
        anime = request.POST["anime"]
        marca = request.POST["marca"]
        fecha_lanzamiento = request.POST["fecha"]
        precio = request.POST["precio"]
        tamano = request.POST["tamano"]
        imagen = request.FILES["imagen"]  # Captura el archivo de imagen enviado en el formulario

        objAnime = Anime.objects.get(id_anime=anime)
        objMarca = Marca.objects.get(id_marca=marca)

        obj = Figura.objects.create(
            nombre_figura=nombre_figura,
            id_anime=objAnime,
            id_marca=objMarca,
            fecha_lanzamiento=fecha_lanzamiento,
            precio=precio,
            tamano=tamano,
            imagen=imagen,  # Asigna el archivo de imagen al campo imagen del modelo Figura
        )
        obj.save()

        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/figura_add.html", context)
@login_required
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
@login_required
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
@login_required
def figura_update(request):
    if request.method=="POST":
        """ 
            Capturo todos los datos del front
            Identificamos
            Asignamos nombre 
        """
        nombre_figura = request.POST["nombre"]
        anime = request.POST["anime"]
        marca = request.POST["marca"]
        fecha_lanzamiento = request.POST["fecha"]
        precio = request.POST["precio"]
        tamano = request.POST["tamano"]


        objAnime = Anime.objects.get(id_anime=anime)
        objMarca= Marca.objects.get(id_marca=marca)

        obj = Figura.objects.create(
            nombre_figura=nombre_figura,
            id_anime=objAnime,
            id_marca=objMarca,
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
def crud_rol(request):
    rols = Rol.objects.all()

    context={
        "rols":rols,
    }
    return render(request,"pages/crud_rol.html",context)
@login_required
def rol_add(request):
    formRol = RolForm()
    formUsuario = UsuarioForm()
    if request.method=="POST":
        nuevo = RolForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()

            context={
                "mensaje":"Agregado con exito",
                "form":formRol
            }
            return render(request,"pages/rol_add.html",context)
    else:
        context = {
            "form":formRol,
            "form2":formUsuario
        }
        return render(request,"pages/rol_add.html",context)
@login_required
def rol_del(request,pk):
    try:
        rol = Rol.objects.get(id_rol=pk)
        rol.delete()

        rols = Rol.objects.all()
        context={
            "mensaje":"Registro eliminado exitosamente",
            "rols":rols
        }
        return render(request,"pages/crud_rol.html",context)
    except:
        rols = Rol.objects.all()
        context={
            "mensaje":"Error, Rol no encontrado...",
            "rols":rols
        }
        return render(request,"pages/crud_rol.html",context)
@login_required
def rol_edit(request,pk):
    if pk!="":
        rol = Rol.objects.get(id_rol=pk)
        form = RolForm(instance=rol)
        if request.method=="POST":
            nuevo = RolForm(request.POST,instance=rol)

            if nuevo.is_valid():
                nuevo.save()

                context ={
                    "mensaje":"Modificado con exito",
                    "form":nuevo
                }
                return render(request,"pages/rol_edit.html",context)
        else:
            context={
                "form":form,
            }
            return render(request,"pages/rol_edit.html",context)
    else:
        rols = Rol.objects.all()
        context={
            "mensaje":"Error, rol no encontrado",
            "rols":rols
        }
        return render(request,"pages/crud_rol.html",context)
@login_required
def crud_anime(request):
    animes = Anime.objects.all()

    context={
        "animes":animes,
    }
    return render(request,"pages/crud_anime.html",context)
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
def loginSession(request):
    if request.method == "POST":
        correo = request.POST.get("username")
        password = request.POST.get("password")
        
        try:
            usuario = Usuario.objects.get(email=correo)
        except Usuario.DoesNotExist:
            usuario = None
        
        if usuario and check_password(password, usuario.password):
            request.session["user"] = usuario.email  # Guarda el email en la sesión
            return redirect('crud')  # Redirige a la vista CRUD (debes definir 'crud' en tus URLs)
        else:
            context = {
                "mensaje": "Usuario o contraseña incorrecta",
                "design": "alert alert-danger w-50 mx-auto text-center",
            }
            return render(request, "pages/login.html", context)
    else:
        context = {}
        return render(request, "pages/login.html", context)

def conectar(request):
    if request.method=="POST":
        correo = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=correo, password=password)
        
        if user is not None:
            login(request, user)
            usuarios = Usuario.objects.all()
            context = {
                "usuarios": usuarios,
            }
            return render(request, "pages/crud.html", context)
        else:
            context = {
                "mensaje": "Usuario o contraseña incorrecta",
                "design": "alert alert-danger w-50 mx-auto text-center",
            }
            return render(request, "pages/login.html", context)
    else:
        context = {}
        return render(request, "pages/login.html", context)

def desconectar(request):
    if request.user.is_authenticated:
        logout(request)
    
    context = {
        "mensaje": "Desconectado con éxito",
        "design": "alert alert-success w-50 mx-auto text-center",
    }
    return render(request, "pages/login.html", context)