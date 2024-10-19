# Generated by Django 5.1.1 on 2024-10-02 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_alter_cliente_direccion_alter_cliente_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
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
