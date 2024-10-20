# Generated by Django 5.1.1 on 2024-10-19 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0041_remove_transaccion_producto_transaccion_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaccion',
            name='productos',
        ),
        migrations.AddField(
            model_name='transaccion',
            name='productos',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='libreria.producto'),
        ),
    ]