from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("catalogo",views.catalogo,name="catalogo"),
    path("iniciosesion",views.iniciosesion,name="iniciosesion"),
    path("registro",views.registro,name="registro"),
    path("kaoricompra",views.kaoricompra,name="kaoricompra"),
    path("preguntasF",views.preguntasF,name="preguntasF"),
    path("somos",views.somos,name="somos"),
    path("crud",views.crud,name="crud"),
    path("user_add",views.user_add,name="user_add"),
    path("crud_genero",views.crud_genero,name="crud_genero"),
    path("genero_add",views.genero_add,name="genero_add"),


]