
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HojaIndicacion', '0004_auto_20200609_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoja_indicaciones',
            name='Hora_cirugias',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hoja_indicaciones',
            name='hora_medicamento',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
