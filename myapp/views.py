from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . models import Vehiculo, Consumo
import re

# Create your views here.
def index(request):
    return render(request, 'index.html')

def pagina_no_encontrada(request, exception):
    return render(request, '404.html', status=404)

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'GET':
        return render(request, 'iniciar_sesion.html')
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'iniciar_sesion.html')

def registro(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'GET':
        return render(request, 'registro.html')
    else:
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        
        # Validar que el email tenga un dominio completo
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            messages.error(request, 'Por favor, introduce un correo electrónico válido con un dominio completo.')
            return render(request, 'registro.html')
        
        if password1 == password2:   
            try:    
                username = request.POST['username']
                user = User.objects.create_user(username, email, password1)
                user.save()
                login(request, user)
                return redirect('index')
            except Exception as e:
                messages.error(request, 'Error al registrarse, el nombre de usuario ya está en uso')
                return render(request, 'registro.html')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'registro.html')
        
def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')

def ecoride(request):
    return render(request, 'ecoride.html')

@login_required
def userProfile(request):
    vehiculos = Vehiculo.objects.filter(user=request.user)
    return render(request, 'profile.html', {
        'vehiculos': vehiculos
    })
@login_required
def registrarVehiculo(request):
    if request.method == 'POST':
        try:    
            print(request.POST)
            vehiculo = Vehiculo.objects.create(marca_modelo=request.POST['marcaModelo'], ano_fabricacion=request.POST['anoFabricacion'], tipo_combustible=request.POST['tipoCombustible'], tamano_motor=request.POST['tamanoMotor'], tipo_transmision=request.POST['tipoTransmision'], user=request.user)
            vehiculo.save()
            print('Vehículo registrado')
            return redirect('profile')
        except Exception as e:
            print(e)
            return render(request, 'profile.html', {'error': f'Error al registrar el vehículo: {e}'})
    else:
        return redirect('profile')
    
def registrarConsumo(request, id):
    if request.method == 'POST':
        try:
            kilometraje_anual = request.POST['kilometrajeAnual']
            consumo_promedio = request.POST['consumoPromedio']
            distancia_promedio = request.POST['distanciaPromedio']
            frecuencia_conduccion = request.POST['frecuenciaConduccion']
            precio_combustible = request.POST['precioCombustible']
            costos_mantenimiento = request.POST['costosMantenimiento']
            impuestos_vehiculares = request.POST['impuestosVehiculares']
            seguros = request.POST['seguros']
            
            vehiculo = Vehiculo.objects.get(id=id, user=request.user)
            consumo = Consumo.objects.create(vehiculo=vehiculo, kilometraje_anual=kilometraje_anual, consumo_promedio=consumo_promedio, distancia_promedio=distancia_promedio, frecuencia_conduccion=frecuencia_conduccion, precio_combustible=precio_combustible, costos_mantenimiento=costos_mantenimiento, impuestos_vehiculares=impuestos_vehiculares, seguros=seguros)
            consumo.save()
            
            consumo_anual = float(kilometraje_anual) * float(consumo_promedio) / 100
            print(f'Consumo anual: {consumo_anual}')
            
            print('Consumo registrado')
            return redirect('evSimulator')
        except Exception as e:
            print(e)
            return render(request, 'calculator.html', {'error': f'Error al registrar el consumo: {e}'})
    else:
        # Manejar solicitudes GET
        return redirect('evSimulator')
    
def evSimulator(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, inicia sesión para acceder al EVsimulator')
        return redirect('iniciar_sesion')
        
    vehiculos = Vehiculo.objects.filter(user=request.user)
    return render(request, 'evsimulator.html', {
        'vehiculos': vehiculos
    })

@login_required    
def calculator(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id, user=request.user)
    return render(request, 'calculator.html', {
        'vehiculo': vehiculo
    })