# Generated by Django 5.0.3 on 2024-03-30 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_entregable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregable',
            name='fecha_de_entrega',
            field=models.DateField(),
        ),
    ]
