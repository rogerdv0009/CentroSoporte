# Generated by Django 5.0.2 on 2024-05-10 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('Especialista', 'Especialista'), ('Cliente', 'Cliente'), ('Administrador', 'Administrador')], default='Cliente', max_length=50, verbose_name='Rol'),
        ),
    ]
