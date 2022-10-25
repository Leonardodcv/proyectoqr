# Generated by Django 4.0.3 on 2022-04-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0013_rename_id_usario_historial_id_usuario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historial',
            name='activo',
        ),
        migrations.AddField(
            model_name='historial',
            name='recibido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='ns',
            field=models.CharField(help_text='Numero serial', max_length=30, primary_key=True, serialize=False, verbose_name='Numero serial'),
        ),
        migrations.AlterField(
            model_name='fabricante',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre del fabricante'),
        ),
        migrations.AlterField(
            model_name='modelo',
            name='nombre',
            field=models.CharField(help_text='Modelo', max_length=200, verbose_name='Modelo de la computadora'),
        ),
        migrations.AlterField(
            model_name='so',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Sistema operativo'),
        ),
        migrations.AlterField(
            model_name='tipo',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Tipo de computadora'),
        ),
    ]
