# Generated by Django 5.1.1 on 2024-10-19 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0042_remove_transaccion_productos_transaccion_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='productos',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='libreria.producto'),
        ),
    ]