# Generated by Django 5.1.2 on 2024-10-30 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='consumo_promedio',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='precio_combustible',
            field=models.PositiveIntegerField(),
        ),
    ]
