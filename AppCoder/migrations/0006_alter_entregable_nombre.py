# Generated by Django 5.0.3 on 2024-03-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_alter_entregable_fecha_de_entrega'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregable',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]