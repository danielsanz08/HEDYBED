# Generated by Django 5.1.1 on 2024-10-02 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_cliente_direccion_cliente_tipo_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo_cliente',
            field=models.CharField(blank=True, choices=[('minorista', 'Minorista'), ('mayorista', 'Mayorista')], max_length=10),
        ),
    ]