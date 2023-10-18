from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from lungHealth_app import views
from lungHealth_app.views import (
    MedicoListado, MedicoDetalle, MedicoCrear, MedicoActualizar, MedicoEliminar,
    PacienteListado, PacienteDetalle, PacienteCrear, PacienteActualizar, PacienteEliminar,
    DiagnosticoListado, DiagnosticoDetalle, DiagnosticoCrear, DiagnosticoActualizar, DiagnosticoEliminar,
    TratamientoListado, TratamientoDetalle, TratamientoCrear, TratamientoActualizar, TratamientoEliminar,
    HospitalListado, HospitalDetalle, HospitalCrear, HospitalActualizar, HospitalEliminar
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

    # URLs para Diagnósticos
    path('diagnosticos/', DiagnosticoListado.as_view(template_name="diagnosticos/index.html"), name='leer_diagnosticos'),
    path('diagnosticos/detalle/<int:pk>/', DiagnosticoDetalle.as_view(template_name="diagnosticos/detalles.html"), name='detalles_diagnostico'),
    path('diagnosticos/crear/', DiagnosticoCrear.as_view(template_name="diagnosticos/crear.html"), name='crear_diagnostico'),
    path('diagnosticos/editar/<int:pk>/', DiagnosticoActualizar.as_view(template_name="diagnosticos/actualizar.html"), name='actualizar_diagnostico'),
    path('diagnosticos/eliminar/<int:pk>/', DiagnosticoEliminar.as_view(template_name="diagnosticos/eliminar.html"), name='eliminar_diagnostico'),

    # URLs para Tratamientos
    path('tratamientos/', TratamientoListado.as_view(template_name="tratamientos/index.html"), name='leer_tratamientos'),
    path('tratamientos/detalle/<int:pk>/', TratamientoDetalle.as_view(template_name="tratamientos/detalles.html"), name='detalles_tratamiento'),
    path('tratamientos/crear/', TratamientoCrear.as_view(template_name="tratamientos/crear.html"), name='crear_tratamiento'),
    path('tratamientos/editar/<int:pk>/', TratamientoActualizar.as_view(template_name="tratamientos/actualizar.html"), name='actualizar_tratamiento'),
    path('tratamientos/eliminar/<int:pk>/', TratamientoEliminar.as_view(template_name="tratamientos/eliminar.html"), name='eliminar_tratamiento'),

    # URLs para Hospitales
    path('hospitales/', HospitalListado.as_view(template_name="hospitales/index.html"), name='leer_hospitales'),
    path('hospitales/detalle/<int:pk>/', HospitalDetalle.as_view(template_name="hospitales/detalles.html"), name='detalles_hospital'),
    path('hospitales/crear/', HospitalCrear.as_view(template_name="hospitales/crear.html"), name='crear_hospital'),
    path('hospitales/editar/<int:pk>/', HospitalActualizar.as_view(template_name="hospitales/actualizar.html"), name='actualizar_hospital'),
    path('hospitales/eliminar/<int:pk>/', HospitalEliminar.as_view(template_name="hospitales/eliminar.html"), name='eliminar_hospital'),
]