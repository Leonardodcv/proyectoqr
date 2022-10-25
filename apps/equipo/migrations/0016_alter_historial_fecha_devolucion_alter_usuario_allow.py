# Generated by Django 4.0.3 on 2022-04-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0015_remove_usuario_aio_usuario_allow_alter_equipo_ns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='fecha_devolucion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de devolucion'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='allow',
            field=models.BooleanField(default=False),
        ),
    ]