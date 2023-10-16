# Generated by Django 4.2.6 on 2023-10-16 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('informacion_contacto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('numero_seguro_social', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('medicamentos_recetados', models.TextField()),
                ('dosificacion', models.CharField(max_length=100)),
                ('duracion_tratamiento', models.CharField(max_length=100)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lungHealth_app.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lungHealth_app.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_diagnostico', models.DateField()),
                ('descripcion', models.TextField()),
                ('resultados_pruebas', models.TextField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lungHealth_app.paciente')),
            ],
        ),
    ]
