# Generated by Django 4.1 on 2022-10-07 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Remedio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('laboratorio', models.CharField(max_length=50)),
                ('fechaIngreso', models.DateField()),
            ],
        ),
    ]
