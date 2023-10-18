# lungHealth App

## Autores
- David Herrera
- Valeria Rudas Ruiz

## Propósito
La aplicación **lungHealth** es una plataforma para la gestión de historias clínicas de pacientes con enfermedades pulmonares en un entorno hospitalario. Su objetivo es facilitar el seguimiento de pacientes, diagnósticos, tratamientos y pruebas médicas relacionadas con enfermedades pulmonares, proporcionando a los profesionales de la salud un sistema eficiente para la atención y el monitoreo de los pacientes.

## Despliegue

### Requisitos previos
- Python 3.x
- Django
- PostgreSQL o el sistema de gestión de bases de datos de tu elección
- Dependencias del proyecto (puedes instalarlas con `pip install -r requirements.txt`)

### Pasos para el despliegue

1. Clona el repositorio desde GitHub:
git clone https://github.com/tuusuario/lungHealth.git


2. Crea un entorno virtual para el proyecto:
python -m venv venv


3. Activa el entorno virtual:
- En Windows:
venv\Scripts\activate

- En macOS y Linux:
source venv/bin/activate


4. Instala las dependencias del proyecto:

pip install -r requirements.txt


5. Configura la base de datos en el archivo `settings.py` y realiza las migraciones:

python manage.py makemigrations
python manage.py migrate


6. Crea un superusuario para acceder a la interfaz de administración de Django:
python manage.py createsuperuser


7. Inicia el servidor de desarrollo:
python manage.py runserver


8. Accede a la aplicación en tu navegador: http://localhost:8000/


9. Inicia sesión con el superusuario que creaste y comienza a utilizar la aplicación.


# ESPECIFICACION DE RAMAS

## Rama: Login
- Creacion y ajuste de las vista inicial
- Creacion de formulario del login
- Redireccionamiento de la vista del login a la proxima vista que estará en la rama de "crud"

