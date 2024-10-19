# Generated by Django 5.1.1 on 2024-10-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0027_alter_cliente_tipo_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo_documento',
            field=models.CharField(choices=[('Cédula de ciudadanía', 'Cédula de ciudadanía'), ('Tarjeta de identidad', 'Tarjeta de identidad'), ('Cédula de extranjería', 'Cédula de extranjería'), ('Pasaporte', 'Pasaporte'), ('NIT', 'Número de Identificación Tributaria (NIT)')], default='cedula_ciudadania', max_length=21),
        ),
    ]