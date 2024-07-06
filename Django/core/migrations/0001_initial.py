# Generated by Django 5.0.6 on 2024-07-06 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id_anime', models.AutoField(db_column='idAnime', primary_key=True, serialize=False)),
                ('anime', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.AutoField(db_column='idMarca', primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Figura',
            fields=[
                ('id_figura', models.AutoField(db_column='idFigura', editable=False, primary_key=True, serialize=False)),
                ('nombre_figura', models.CharField(max_length=40)),
                ('fecha_lanzamiento', models.DateField()),
                ('precio', models.IntegerField()),
                ('tamano', models.CharField(max_length=20)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='figuras/')),
                ('id_anime', models.ForeignKey(db_column='idAnime', on_delete=django.db.models.deletion.CASCADE, to='core.anime')),
                ('id_marca', models.ForeignKey(db_column='idMarca', on_delete=django.db.models.deletion.CASCADE, to='core.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('id_genero', models.ForeignKey(db_column='idGenero', on_delete=django.db.models.deletion.CASCADE, to='core.genero')),
            ],
        ),
        migrations.CreateModel(
            name='CarritoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('figura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.figura')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
    ]
