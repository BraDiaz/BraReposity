# Generated by Django 2.2.5 on 2019-11-16 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appcafeteria', '0008_auto_20191115_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='producto_comprado',
            new_name='producto',
        ),
    ]
