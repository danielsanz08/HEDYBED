# Generated by Django 5.1.1 on 2024-10-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0024_alter_producto_fecha_elaboracion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='documento',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_documento',
            field=models.CharField(choices=[('cedula_ciudadania', 'Cédula de ciudadanía'), ('tarjeta_identidad', 'Tarjeta de identidad'), ('cedula_extranjeria', 'Cédula de extranjería'), ('pasaporte', 'Pasaporte'), ('nit', 'Número de Identificación Tributaria (NIT)')], default='cedula_ciudadania', max_length=20),
        ),
    ]
