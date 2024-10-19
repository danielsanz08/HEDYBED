# Generated by Django 5.1.1 on 2024-10-10 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0016_transaccion_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaccion',
            name='producto',
        ),
        migrations.AddField(
            model_name='transaccion',
            name='producto',
            field=models.ManyToManyField(to='libreria.producto'),
        ),
    ]