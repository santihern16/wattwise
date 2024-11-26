from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
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
        return render(request, 'registrarse.html')
    else:
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        
        # Validar que el email tenga un dominio completo
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            messages.error(request, 'Por favor, introduce un correo electrónico válido con un dominio completo.')
            return render(request, 'registrarse.html')
        
        if password1 == password2:   
            try:    
                username = request.POST['username']
                user = User.objects.create_user(username, email, password1)
                user.save()
                login(request, user)
                return redirect('index')
            except Exception as e:
                messages.error(request, 'Error al registrarse, el nombre de usuario ya está en uso')
                return render(request, 'registrarse.html')
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'registrarse.html')
        
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

@login_required
def registrarConsumo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id, user=request.user)
    
    if request.method == 'GET':
        return render(request, 'calculator.html', {
            'vehiculo': vehiculo
        })
    else:
        try:
            consumo = Consumo.objects.create(vehiculo=vehiculo, kilometraje_anual=request.POST['kilometrajeAnual'], consumo_promedio=request.POST['consumoPromedio'], distancia_promedio=request.POST['distanciaPromedio'], frecuencia_conduccion=request.POST['frecuenciaConduccion'], precio_combustible=request.POST['precioCombustible'], costos_mantenimiento=request.POST['costosMantenimiento'], impuestos_vehiculares=request.POST['impuestosVehiculares'], seguros=request.POST['seguros'])
            consumo.save()
            return redirect('mostrarResultados', id=consumo.id)
        except Exception as e:
            return render(request, 'calculator.html', {
                'vehiculo': vehiculo,
                'error': f'Error al registrar el consumo: {e}'
            })
    
def evSimulator(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, inicia sesión para acceder al EVsimulator')
        return redirect('iniciar_sesion')
        
    vehiculos = Vehiculo.objects.filter(user=request.user)
    return render(request, 'evsimulator.html', {
        'vehiculos': vehiculos
    })

@login_required    
def mostrarRegistroConsumo(request, id):
    consumo = get_object_or_404(Consumo, id=id, vehiculo__user=request.user)
    
    consumo_anual = consumo.kilometraje_anual * consumo.consumo_promedio / 100
    costo_anual_combustible = float(consumo_anual * consumo.precio_combustible)
    costo_fijo_anual = consumo.costos_mantenimiento + consumo.impuestos_vehiculares + consumo.seguros
    costo_total_anual = float(costo_anual_combustible + costo_fijo_anual)
    
    calculos = []
    calculos.append({
        'consumo_anual': consumo_anual,
        'costo_anual_combustible': costo_anual_combustible,
        'costo_fijo_anual': costo_fijo_anual,
        'costo_total_anual': costo_total_anual,
    })
    return render(request, 'resultados.html', {
        'consumo': consumo,
        'calculos': calculos
    })

@login_required    
def mostrarHistorialConsumos(request):
    consumos = Consumo.objects.filter(vehiculo__user=request.user)
    calculos = []
    
    for consumo in consumos:
        consumo_anual = consumo.kilometraje_anual * consumo.consumo_promedio / 100
        costo_anual_combustible = float(consumo_anual * consumo.precio_combustible)
        costo_fijo_anual = consumo.costos_mantenimiento + consumo.impuestos_vehiculares + consumo.seguros
        costo_total_anual = float(costo_anual_combustible + costo_fijo_anual)
        
        calculos.append({
            'consumo': consumo,
            'consumo_anual': consumo_anual,
            'costo_anual_combustible': costo_anual_combustible,
            'costo_fijo_anual': costo_fijo_anual,
            'costo_total_anual': costo_total_anual,
            'vehiculo': consumo.vehiculo.marca_modelo,
        })
    return render(request, 'historialConsumos.html', {
        'consumos': consumos,
        'calculos': calculos
        })

@login_required
def mostrarRegistroPorVehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id, user=request.user)
    consumos = Consumo.objects.filter(vehiculo=vehiculo)
        
    calculos = []
    
    for consumo in consumos:
        consumo_anual = consumo.kilometraje_anual * consumo.consumo_promedio / 100
        costo_anual_combustible = float(consumo_anual * consumo.precio_combustible)
        costo_fijo_anual = consumo.costos_mantenimiento + consumo.impuestos_vehiculares + consumo.seguros
        costo_total_anual = float(costo_anual_combustible + costo_fijo_anual)
        
        calculos.append({
            'consumo': consumo,
            'consumo_anual': consumo_anual,
            'costo_anual_combustible': costo_anual_combustible,
            'costo_fijo_anual': costo_fijo_anual,
            'costo_total_anual': costo_total_anual,
            'vehiculo': consumo.vehiculo.marca_modelo,
        })
    return render(request, 'registroPorId.html', {
        'vehiculo': vehiculo,
        'calculos': calculos
    })

def pagina_vehiculos(request):
    return render(request, 'vehiculos.html')

def fordF(request):
    return render(request, 'fordf150.html')

def fordMustang(request):
    return render(request, 'FordMustang.html')

def fordExplorer(request):
    return render(request, 'FordExplorer.html')

def fordEscape(request):
    return render(request, 'FordEscape.html')

def teslaSPlaid(request):
    return render(request, 'TeslaSPlaid.html')

def teslaCybertruck(request):
    return render(request, 'TeslaCybertruck.html')

def nosotros(request):
    return render(request, 'Nosotros.html')