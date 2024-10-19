# Generated by Django 5.1.1 on 2024-10-19 22:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0038_transaccion_producto_alter_transaccion_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaccion',
            name='producto',
        ),
        migrations.AddField(
            model_name='transaccion',
            name='productos',
            field=models.ManyToManyField(to='libreria.producto'),
        ),
        migrations.CreateModel(
            name='LineaTransaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.producto')),
                ('transaccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.transaccion')),
            ],
        ),
    ]