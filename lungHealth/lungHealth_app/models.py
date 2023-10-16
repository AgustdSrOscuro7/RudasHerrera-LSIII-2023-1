from django.db import models
from django.contrib.auth.models import User

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)
    usuarios_asociados = models.ManyToManyField('User')

class Meta:
    db_table = 'medicos'
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    numero_seguro_social = models.CharField(max_length=20, unique=True)
    medico_asignado = models.ForeignKey(User, on_delete=models.CASCADE)

class Meta:
    db_table = 'pacientes'

class Diagnostico(models.Model):
    fecha_diagnostico = models.DateField()
    descripcion = models.TextField()
    resultados_pruebas = models.TextField()
    medico = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class Meta:
    db_table = 'diagnosticos'

class Tratamiento(models.Model):
    fecha_inicio = models.DateField()
    medicamentos_recetados = models.TextField()
    dosificacion = models.CharField(max_length=100)
    duracion_tratamiento = models.CharField(max_length=100)
    medico = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class Meta:
    db_table = 'tratamientos'

class Hospital(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    informacion_contacto = models.TextField()

class Meta:
    db_table = 'hospitales'