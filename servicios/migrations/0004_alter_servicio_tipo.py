# Generated by Django 5.0.2 on 2024-05-10 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_alter_servicio_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='tipo',
            field=models.CharField(choices=[('Especializados', 'Especializados'), ('Otro', 'Otro'), ('Online', 'Online')], max_length=50, verbose_name='Tipo'),
        ),
    ]
