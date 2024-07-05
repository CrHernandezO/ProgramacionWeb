from django.urls import path
from core import views

urlpatterns=[
    path("",views.index,name="index"),
    path("catalogo",views.catalogo,name="catalogo"),
    path("iniciosesion",views.iniciosesion,name="iniciosesion"),
    path("registro",views.registro,name="registro"),
    path("kaoricompra",views.kaoricompra,name="kaoricompra"),
    path("preguntasF",views.preguntasF,name="preguntasF"),
    path("somos",views.somos,name="somos"),
    path("crud", views.crud, name="crud"),
    path("user_add", views.user_add, name="user_add"),
    path("user_del/<str:pk>", views.user_del, name="user_del"),
    path("user_findEdit/<str:pk>", views.user_findEdit, name="user_findEdit"),
    path("user_update", views.user_update, name="user_update"),
    path("crud_genero", views.crud_genero, name="crud_genero"),
    path("genero_add", views.genero_add, name="genero_add"),
    path("genero_del/<str:pk>", views.genero_del, name="genero_del"),
    path("genero_edit/<str:pk>", views.genero_edit, name="genero_edit"),
    path("login", views.conectar, name="login"),
    path("logout", views.desconectar, name="logout"),

]