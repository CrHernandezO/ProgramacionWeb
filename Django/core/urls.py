from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('agregar_al_carrito/<int:figura_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.carrito, name='carrito'),
    path('iniciocliente/', views.iniciocliente, name='iniciocliente'),
    path("registro/", views.registro, name="registro"),
    path("kaoricompra/", views.kaoricompra, name="kaoricompra"),
    path("preguntasF/", views.preguntasF, name="preguntasF"),
    path("somos/", views.somos, name="somos"),
    path("crud/", views.crud, name="crud"),
    path("user_add/", views.user_add, name="user_add"),
    path("user_del/<str:pk>/", views.user_del, name="user_del"),
    path("user_findEdit/<str:pk>/", views.user_findEdit, name="user_findEdit"),
    path("user_update/", views.user_update, name="user_update"),
    path("crud_figura/", views.crud_figura, name="crud_figura"),
    path("figura_add/", views.figura_add, name="figura_add"),
    path("figura_del/<str:pk>/", views.figura_del, name="figura_del"),
    path("figura_findEdit/<str:pk>/", views.figura_findEdit, name="figura_findEdit"),
    path("figura_update/", views.figura_update, name="figura_update"),
    path("crud_rol/", views.crud_rol, name="crud_rol"),
    path("rol_add/", views.rol_add, name="rol_add"),
    path("rol_del/<str:pk>/", views.rol_del, name="rol_del"),
    path("rol_edit/<str:pk>/", views.rol_edit, name="rol_edit"),
    path("crud_anime/", views.crud_anime, name="crud_anime"),
    path("anime_add/", views.anime_add, name="anime_add"),
    path("anime_del/<str:pk>/", views.anime_del, name="anime_del"),
    path("anime_edit/<str:pk>/", views.anime_edit, name="anime_edit"),
    path("crud_marca/", views.crud_marca, name="crud_marca"),
    path("marca_add/", views.marca_add, name="marca_add"),
    path("marca_del/<str:pk>/", views.marca_del, name="marca_del"),
    path("marca_edit/<str:pk>/", views.marca_edit, name="marca_edit"),
    path("login/", views.conectar, name="login"),
    path("logout/", views.desconectar, name="logout"),
    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('restar_del_carrito/<int:item_id>/', views.restar_del_carrito, name='restar_del_carrito'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
