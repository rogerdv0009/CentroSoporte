# Generated by Django 5.0.2 on 2024-05-15 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['-id'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]
