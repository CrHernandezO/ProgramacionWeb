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
    activo= models.BooleanField()
    def __str__(self):
        return str(self.nombre)+" "+ str(self.apellido_paterno)+ " "+ str(self.apellido_materno)


class Figura(models.Model):
    nombre_figura = models.CharField(max_length=20)
    anime = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    fecha_lanzamiento = models.DateField(blank=False, null=False)
    precio=models.IntegerField()
    tamano=models.CharField(max_length=20)
    id_figura = models.IntegerField( editable=False,primary_key=True)
    def asignar_numero_secuencia(sender, instance, **kwargs):
        if not instance.id_figura:
            ultimo_registro = Figura.objects.last()
            if ultimo_registro:
                instance.id_figura = ultimo_registro.id_figura + 1
            else:
                instance.id_figura = 1
    def __str__(self):
        return str(self.nombre_figura)+" "+ str(self.anime)+ " "+ str(self.id_figura)