# Generated by Django 5.1.2 on 2024-10-30 21:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_modelo', models.CharField(max_length=100)),
                ('ano_fabricacion', models.PositiveIntegerField()),
                ('tipo_combustible', models.CharField(choices=[('gasolina', 'Gasolina'), ('diesel', 'Diésel'), ('gas_natural', 'Gas natural')], max_length=20)),
                ('tamano_motor', models.PositiveIntegerField()),
                ('tipo_transmision', models.CharField(choices=[('manual', 'Manual'), ('automatica', 'Automática')], max_length=20)),
                ('kilometraje_anual', models.PositiveIntegerField()),
                ('consumo_promedio', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('distancia_promedio', models.PositiveIntegerField()),
                ('frecuencia_conduccion', models.CharField(choices=[('diaria', 'Diaria'), ('semanal', 'Semanal'), ('mensual', 'Mensual')], max_length=20)),
                ('precio_combustible', models.DecimalField(decimal_places=2, max_digits=5)),
                ('costos_mantenimiento', models.PositiveIntegerField()),
                ('impuestos_vehiculares', models.PositiveIntegerField()),
                ('seguros', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
