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
]