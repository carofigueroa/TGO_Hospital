# Generated by Django 3.0.7 on 2020-06-17 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HojaIndicacion', '0007_auto_20200616_1922'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agenda_matrona',
            options={'verbose_name_plural': 'Agenda'},
        ),
        migrations.AddField(
            model_name='agenda_matrona',
            name='nombre_profesional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HojaIndicacion.profesional'),
        ),
        migrations.AlterField(
            model_name='hoja_indicaciones',
            name='hora_examen',
            field=models.TimeField(blank=True, null=True),
        ),
    ]