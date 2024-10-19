# Generated by Django 5.1.1 on 2024-10-10 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('libreria', '0012_alter_proveedor_nit_alter_transaccion_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='Los grupos a los que pertenece este usuario.', related_name='customuser_set', to='auth.group', verbose_name='grupos'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Permisos específicos para este usuario.', related_name='customuser_permissions_set', to='auth.permission', verbose_name='permisos del usuario'),
        ),
    ]