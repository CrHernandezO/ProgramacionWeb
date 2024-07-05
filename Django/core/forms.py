from django import forms
from .models import Genero, Usuario,Anime,Marca

from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
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