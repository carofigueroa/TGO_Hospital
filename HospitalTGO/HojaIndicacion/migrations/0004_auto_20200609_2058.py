
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HojaIndicacion', '0003_auto_20200609_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='examene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_examen', models.CharField(max_length=50)),
                ('tipo_examen', models.CharField(max_length=20)),
                ('especificaciones', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='diagnostico',
        ),
        migrations.AlterField(
            model_name='hoja_indicaciones',
            name='examen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HojaIndicacion.examene'),
        ),
        migrations.DeleteModel(
            name='examenes',
        ),
    ]
