# Generated by Django 4.0.6 on 2022-08-19 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juego', '0002_alter_usuario_preguntasacertadas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tiempo',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
