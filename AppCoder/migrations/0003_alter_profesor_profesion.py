# Generated by Django 5.0.3 on 2024-03-29 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_alumno_profesor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='profesion',
            field=models.CharField(max_length=30),
        ),
    ]
