# Generated by Django 5.0.2 on 2024-05-08 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('solicitud', '0001_initial'),
        ('soporte', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud_soporte',
            name='id_soporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soporte.soporte', verbose_name='Plan Soporte'),
        ),
    ]
