# Generated by Django 4.1.7 on 2023-04-04 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_juegos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juegos',
            name='descripcion',
            field=models.TextField(max_length=500),
        ),
    ]
