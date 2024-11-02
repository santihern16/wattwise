from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vehiculo(models.Model):
    marca_modelo = models.CharField(max_length=100)
    ano_fabricacion = models.PositiveIntegerField()
    TIPO_COMBUSTIBLE_CHOICES = [
        ('gasolina', 'Gasolina'),
        ('diesel', 'Diésel'),
        ('gas_natural', 'Gas natural'),
    ]
    tipo_combustible = models.CharField(max_length=20, choices=TIPO_COMBUSTIBLE_CHOICES)
    tamano_motor = models.PositiveIntegerField()
    TIPO_TRANSMISION_CHOICES = [
        ('manual', 'Manual'),
        ('automatica', 'Automática'),
    ]
    tipo_transmision = models.CharField(max_length=20, choices=TIPO_TRANSMISION_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.marca_modelo
    
class Consumo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    kilometraje_anual = models.PositiveIntegerField()
    consumo_promedio = models.DecimalField(max_digits=5, decimal_places=2)
    distancia_promedio = models.PositiveIntegerField()
    FRECUENCIA_CONDUCCION_CHOICES = [
        ('diaria', 'Diaria'),
        ('semanal', 'Semanal'),
        ('mensual', 'Mensual'),
    ]
    frecuencia_conduccion = models.CharField(max_length=20, choices=FRECUENCIA_CONDUCCION_CHOICES)
    precio_combustible = models.PositiveIntegerField()
    costos_mantenimiento = models.PositiveIntegerField()
    impuestos_vehiculares = models.PositiveIntegerField()
    seguros = models.PositiveIntegerField()