# Generated by Django 4.0.3 on 2022-04-28 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0017_alter_usuario_options_equipo_basura_electronica_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='puesto',
            field=models.CharField(default='Estandar', max_length=50),
        ),
    ]
