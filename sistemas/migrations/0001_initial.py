# Generated by Django 5.0.2 on 2024-05-08 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creado', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_modificado', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('siglas', models.CharField(max_length=10, verbose_name='Siglas')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Sistema',
                'verbose_name_plural': 'Sistemas',
                'ordering': ['-id'],
            },
        ),
    ]
