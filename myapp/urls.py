from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('register/', views.registro, name='registro'),
    path('ecoride/', views.ecoride, name='ecoride'),
    path('profile/', views.userProfile, name='profile'),
    path('profile/registrarVehiculo/', views.registrarVehiculo, name='registrarVehiculo'),
    path('evsimulator/', views.evSimulator, name='evSimulator'),
    #path('evsimulator/calculator/<int:id>', views.calculator, name='calculator'),
    path('evsimulator/registrarConsumo/<int:id>/', views.registrarConsumo, name='registrarConsumo'),
    path('resultados/<int:id>/', views.mostarResultados, name='mostrarResultados'),
    path('resultados/', views.mostrarTodosLosResultados, name='mostrarTodosLosResultados'),
    path('registroPorVehiculo/<int:id>/', views.mostrarRegistroPorId, name='registroPorVehiculo'),
]

handler404 = 'myapp.views.pagina_no_encontrada'