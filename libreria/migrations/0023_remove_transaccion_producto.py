# Generated by Django 5.1.1 on 2024-10-10 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0022_alter_transaccion_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaccion',
            name='producto',
        ),
    ]
