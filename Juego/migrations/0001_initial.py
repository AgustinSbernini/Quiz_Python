# Generated by Django 4.0.6 on 2022-08-18 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=50)),
                ('preguntasAcertadas', models.CharField(default='00/20', max_length=10)),
                ('tiempo', models.TimeField()),
                ('puntaje', models.IntegerField(default=0)),
            ],
        ),
    ]
