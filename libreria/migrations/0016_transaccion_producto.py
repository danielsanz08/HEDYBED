# Generated by Django 5.1.1 on 2024-10-10 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0015_producto_categoria_producto_fecha_elaboracion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='libreria.producto'),
        ),
    ]