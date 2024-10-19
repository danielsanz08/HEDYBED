# Generated by Django 5.1.1 on 2024-10-16 18:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0028_alter_cliente_tipo_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='registrado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]