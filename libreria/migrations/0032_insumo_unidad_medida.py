# Generated by Django 5.1.1 on 2024-10-16 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0031_alter_proveedor_tipo_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='insumo',
            name='unidad_medida',
            field=models.CharField(choices=[('kilogramo', 'Kilogramo (kg)'), ('gramo', 'Gramo (g)'), ('litro', 'Litro (l)'), ('mililitro', 'Mililitro (ml)'), ('unidad', 'Unidad')], default='unidad', max_length=15),
        ),
    ]