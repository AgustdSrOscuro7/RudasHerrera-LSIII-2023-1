from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from lungHealth_app import views
from lungHealth_app.views import (
    MedicoListado, MedicoDetalle, MedicoCrear, MedicoActualizar, MedicoEliminar,
    PacienteListado, PacienteDetalle, PacienteCrear, PacienteActualizar, PacienteEliminar,
    TratamientoListado, TratamientoDetalle, TratamientoCrear, TratamientoActualizar, TratamientoEliminar
)

urlpatterns = [
    #path('', RedirectView.as_view(url=reverse_lazy('crear_medico')), name='inicio'),  # Redireccionar página de inicio a creación de médicos

    #LANDING:
    path('', views.inicio),
    
    #ENTRAR A LOGIN:
    path('login/', views.login, name='login'),
    
    #ELEGIR MODELOS SEGUN SE DESEE
    path('elegirModelos/', views.elegirModelos, name='elegirModelos'),
    
    # URLs para Médicos
    path('admin/', admin.site.urls),
    path('medicos/', MedicoListado.as_view(template_name="medicos/index.html"), name='leer_medicos'),
    path('medicos/detalle/<int:pk>/', MedicoDetalle.as_view(template_name="medicos/detalles.html"), name='detalles_medico'),
    path('medicos/crear/', MedicoCrear.as_view(template_name="medicos/crear.html"), name='crear_medico'),
    path('medicos/editar/<int:pk>/', MedicoActualizar.as_view(template_name="medicos/actualizar.html"), name='actualizar_medico'),
    path('medicos/eliminar/<int:pk>/', MedicoEliminar.as_view(template_name="medicos/eliminar.html"), name='eliminar_medico'),

    # URLs para Pacientes
    path('pacientes/', PacienteListado.as_view(template_name="pacientes/indexP.html"), name='leer_pacientes'),
    path('pacientes/detalleP/<int:pk>/', PacienteDetalle.as_view(template_name="pacientes/detallesP.html"), name='detalles_paciente'),
    path('pacientes/crearP/', PacienteCrear.as_view(template_name="pacientes/crearP.html"), name='crear_paciente'),
    path('pacientes/editarP/<int:pk>/', PacienteActualizar.as_view(template_name="pacientes/actualizarP.html"), name='actualizar_paciente'),
    path('pacientes/eliminarP/<int:pk>/', PacienteEliminar.as_view(template_name="pacientes/eliminarP.html"), name='eliminar_paciente'),
    
    # URLs para Tratamientos
    path('tratamientos/', TratamientoListado.as_view(template_name="tratamientos/indexT.html"), name='leer_tratamientos'),
    path('tratamientos/detalleT/<int:pk>/', TratamientoDetalle.as_view(template_name="tratamientos/detallesT.html"), name='detalles_tratamiento'),
    path('tratamientos/crearT/', TratamientoCrear.as_view(template_name="tratamientos/crearT.html"), name='crear_tratamiento'),
    path('tratamientos/editarT/<int:pk>/', TratamientoActualizar.as_view(template_name="tratamientos/actualizarT.html"), name='actualizar_tratamiento'),
    path('tratamientos/eliminarT/<int:pk>/', TratamientoEliminar.as_view(template_name="tratamientos/eliminarT.html"), name='eliminar_tratamiento')

]