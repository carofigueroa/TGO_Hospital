# Generated by Django 3.0.7 on 2020-08-03 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HojaIndicacion', '0010_hoja_indicaciones_alta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hoja_indicaciones',
            name='Hora_cirugias',
        ),
        migrations.RemoveField(
            model_name='hoja_indicaciones',
            name='hora_examen',
        ),
        migrations.AddField(
            model_name='hoja_indicaciones',
            name='cirugias',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hoja_indicaciones',
            name='examen',
            field=models.BooleanField(default=False),
        ),
    ]
