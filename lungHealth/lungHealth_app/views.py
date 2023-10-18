from django.shortcuts import render
from .models import Medico, Paciente, Diagnostico, Tratamiento, Hospital
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

def inicio(request):
    return render(request, 'inicio.html')

def login(request):
    return render(request, 'login.html')

def elegirModelos(request):
    return render(request, 'elegirModelos.html')

# Vistas para Médicos
class MedicoListado(ListView):
    model = Medico

class MedicoCrear(SuccessMessageMixin, CreateView):
    model = Medico
    fields = "__all__"
    success_message = 'Médico Creado Correctamente!'

    def get_success_url(self):
        return reverse('leer_medicos')

class MedicoDetalle(DetailView):
    model = Medico

class MedicoActualizar(SuccessMessageMixin, UpdateView):
    model = Medico
    fields = "__all__"
    success_message = 'Médico Actualizado Correctamente!'

    def get_success_url(self):
        return reverse('leer_medicos')

class MedicoEliminar(SuccessMessageMixin, DeleteView):
    model = Medico

    def get_success_url(self):
        success_message = 'Médico Eliminado Correctamente!'
        messages.success(self.request, success_message)
        return reverse('leer_medicos')

# Vistas para Pacientes
class PacienteListado(ListView):
    model = Paciente

class PacienteCrear(SuccessMessageMixin, CreateView):
    model = Paciente
    fields = "__all__"
    success_message = 'Paciente Creado Correctamente!'

    def get_success_url(self):
        return reverse('leer_pacientes')

class PacienteDetalle(DetailView):
    model = Paciente

class PacienteActualizar(SuccessMessageMixin, UpdateView):
    model = Paciente
    fields = "__all__"
    success_message = 'Paciente Actualizado Correctamente!'

    def get_success_url(self):
        return reverse('leer_pacientes')

class PacienteEliminar(SuccessMessageMixin, DeleteView):
    model = Paciente

    def get_success_url(self):
        success_message = 'Paciente Eliminado Correctamente!'
        messages.success(self.request, success_message)
        return reverse('leer_pacientes')

# Vistas para Diagnósticos
class DiagnosticoListado(ListView):
    model = Diagnostico

class DiagnosticoCrear(SuccessMessageMixin, CreateView):
    model = Diagnostico
    fields = "__all__"
    success_message = 'Diagnóstico Creado Correctamente!'

    def get_success_url(self):
        return reverse('leer_diagnosticos')

class DiagnosticoDetalle(DetailView):
    model = Diagnostico

class DiagnosticoActualizar(SuccessMessageMixin, UpdateView):
    model = Diagnostico
    fields = "__all__"
    success_message = 'Diagnóstico Actualizado Correctamente!'

    def get_success_url(self):
        return reverse('leer_diagnosticos')

class DiagnosticoEliminar(SuccessMessageMixin, DeleteView):
    model = Diagnostico

    def get_success_url(self):
        success_message = 'Diagnóstico Eliminado Correctamente!'
        messages.success(self.request, success_message)
        return reverse('leer_diagnosticos')

# Vistas para Tratamientos
class TratamientoListado(ListView):
    model = Tratamiento

class TratamientoCrear(SuccessMessageMixin, CreateView):
    model = Tratamiento
    fields = "__all__"
    success_message = 'Tratamiento Creado Correctamente!'

    def get_success_url(self):
        return reverse('leer_tratamientos')

class TratamientoDetalle(DetailView):
    model = Tratamiento

class TratamientoActualizar(SuccessMessageMixin, UpdateView):
    model = Tratamiento
    fields = "__all__"
    success_message = 'Tratamiento Actualizado Correctamente!'

    def get_success_url(self):
        return reverse('leer_tratamientos')

class TratamientoEliminar(SuccessMessageMixin, DeleteView):
    model = Tratamiento

    def get_success_url(self):
        success_message = 'Tratamiento Eliminado Correctamente!'
        messages.success(self.request, success_message)
        return reverse('leer_tratamientos')


# Vistas para Hospitales
class HospitalListado(ListView):
    model = Hospital

class HospitalCrear(SuccessMessageMixin, CreateView):
    model = Hospital
    fields = "__all__"
    success_message = 'Hospital Creado Correctamente!'

    def get_success_url(self):
        return reverse('leer_hospitales')

class HospitalDetalle(DetailView):
    model = Hospital

class HospitalActualizar(SuccessMessageMixin, UpdateView):
    model = Hospital
    fields = "__all__"
    success_message = 'Hospital Actualizado Correctamente!'

    def get_success_url(self):
        return reverse('leer_hospitales')

class HospitalEliminar(SuccessMessageMixin, DeleteView):
    model = Hospital

    def get_success_url(self):
        success_message = 'Hospital Eliminado Correctamente!'
        messages.success(self.request, success_message)
        return reverse('leer_hospitales')
