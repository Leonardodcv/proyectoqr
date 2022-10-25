# Generated by Django 4.0.3 on 2022-04-12 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0005_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impresora',
            fields=[
                ('ns', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('folio', models.CharField(blank=True, default='N/A', max_length=15, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipo.departamento')),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipo.fabricante')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipo.modelo')),
            ],
            options={
                'verbose_name': 'Impresora',
                'verbose_name_plural': 'Impresoras',
                'ordering': ['ns'],
            },
        ),
        migrations.CreateModel(
            name='Escaner',
            fields=[
                ('ns', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('folio', models.CharField(blank=True, default='N/A', max_length=15, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipo.departamento')),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipo.fabricante')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipo.modelo')),
            ],
            options={
                'verbose_name': 'Escaner',
                'verbose_name_plural': 'Escaneres',
                'ordering': ['ns'],
            },
        ),
    ]
