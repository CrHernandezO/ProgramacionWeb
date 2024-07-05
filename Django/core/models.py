from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.

class Genero(models.Model):
    id_genero= models.AutoField(db_column="idGenero",primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)


    def __str__(self):
        return str(self.genero)

class Usuario(models.Model):
    rut = models.CharField(max_length=20,primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey("Genero", on_delete= models.CASCADE , db_column = "idGenero")
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique = True,max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return str(self.nombre)+" "+ str(self.apellido_paterno)+ " "+ str(self.apellido_materno)


class Figura(models.Model):
    id_figura = models.AutoField( db_column="idFigura",editable=False,primary_key=True)
    nombre_figura = models.CharField(max_length=20)
    id_anime = models.ForeignKey("Anime", on_delete= models.CASCADE , db_column = "idAnime")
    id_marca = models.ForeignKey("Marca", on_delete= models.CASCADE , db_column = "idMarca")
    fecha_lanzamiento = models.DateField(blank=False, null=False)
    precio=models.IntegerField()
    tamano=models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre_figura)+" "+ str(self.anime)+ " "+ str(self.id_figura)
    
class Anime(models.Model):
    id_anime= models.AutoField(db_column="idAnime",primary_key=True)
    anime = models.CharField(max_length=20, blank=False, null=False)


    def __str__(self):
        return str(self.anime)

class Marca(models.Model):
    id_marca= models.AutoField(db_column="idMarca",primary_key=True)
    marca = models.CharField(max_length=20, blank=False, null=False)


    def __str__(self):
        return str(self.marca)