# Generated by Django 4.1.5 on 2023-01-05 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Colegio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignaturas',
            name='cod_asignatura',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
