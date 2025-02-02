# Generated by Django 5.0.7 on 2024-07-18 01:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, unique=True)),
                ('apellido', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, unique=True)),
                ('hora', models.TimeField(blank=True)),
                ('aula', models.CharField(max_length=30, unique=True)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrera.clase')),
                ('maestro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrera.maestro')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=12, unique=True)),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrera.seccion')),
            ],
        ),
    ]
