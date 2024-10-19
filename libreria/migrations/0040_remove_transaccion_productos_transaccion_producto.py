# Generated by Django 5.1.1 on 2024-10-19 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0039_remove_transaccion_producto_transaccion_productos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaccion',
            name='productos',
        ),
        migrations.AddField(
            model_name='transaccion',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='libreria.producto'),
        ),
    ]