from django import forms
from .models import Rol, Usuario,Anime,Marca

from django.forms import ModelForm

class RolForm(ModelForm):
    class Meta:
        model = Rol
        fields = "__all__"

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class AnimeForm(ModelForm):
    class Meta:
        model = Anime
        fields = "__all__"

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = "__all__"