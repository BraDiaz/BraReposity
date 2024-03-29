# Generated by Django 2.2.7 on 2019-11-14 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Appcafeteria', '0003_auto_20191114_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='detalle',
        ),
        migrations.AddField(
            model_name='factura',
            name='id_articulo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Appcafeteria.Articulo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='factura',
            name='total',
            field=models.DecimalField(decimal_places=2, default=125.0, max_digits=12, verbose_name='Total'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='detalleVenta',
        ),
    ]
