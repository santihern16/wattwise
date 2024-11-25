from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('signup/', views.registro, name='registro'),
    path('vehiculos/', views.pagina_vehiculos, name='vehiculos'),
    path('vehiculos/fordf150/', views.fordF, name='fordF'),
    path('vehiculos/FordMustang/', views.fordMustang, name='fordMustang'),
    path('profile/', views.userProfile, name='profile'),
    path('profile/registrarVehiculo/', views.registrarVehiculo, name='registrarVehiculo'),
    path('evsimulator/', views.evSimulator, name='evSimulator'),
    path('evsimulator/registrarConsumo/<int:id>/', views.registrarConsumo, name='registrarConsumo'),
    path('registro/<int:id>/', views.mostrarRegistroConsumo, name='mostrarResultados'),
    path('historialCalculos/', views.mostrarHistorialConsumos, name='mostrarTodosLosResultados'),
    path('registroPorVehiculo/<int:id>/', views.mostrarRegistroPorVehiculo, name='registroPorVehiculo'),
]

handler404 = 'myapp.views.pagina_no_encontrada'