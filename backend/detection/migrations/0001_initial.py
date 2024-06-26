# Generated by Django 4.2.13 on 2024-06-21 14:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=255)),
                ('unidad', models.CharField(blank=True, max_length=255)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='image/materials')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiales',
                'db_table': 'materials',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('director_proyecto', models.CharField(blank=True, max_length=100)),
                ('administrador', models.CharField(blank=True, max_length=100)),
                ('cliente', models.CharField(blank=True, max_length=100)),
                ('estado', models.CharField(blank=True, choices=[('Activo', 'Activo'), ('En liquidación', 'En liquidación'), ('Inactivo', 'Inactivo'), ('Suspendido', 'Suspendido'), ('Terminado', 'Terminado')], default='Activo', max_length=50)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'db_table': 'projects',
            },
        ),
        migrations.CreateModel(
            name='SST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(blank=True, max_length=255)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='image/sst')),
            ],
            options={
                'verbose_name': 'SST',
                'verbose_name_plural': 'SST',
                'db_table': 'sst',
            },
        ),
        migrations.CreateModel(
            name='TypeSigns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='image/signs')),
            ],
            options={
                'verbose_name': 'Tipo Señal',
                'verbose_name_plural': 'Tipos Señales',
                'db_table': 'types_signs',
            },
        ),
        migrations.CreateModel(
            name='Signs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=255)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signs', to='detection.typesigns')),
            ],
            options={
                'verbose_name': 'Señal',
                'verbose_name_plural': 'Señales',
                'db_table': 'signs',
            },
        ),
        migrations.CreateModel(
            name='DetectionSST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_original', models.ImageField(blank=True, null=True, upload_to='original/sst')),
                ('imagen_procesada', models.ImageField(blank=True, null=True, upload_to='procesada/sst')),
                ('descripcion', models.CharField(blank=True, max_length=255)),
                ('latitud', models.DecimalField(blank=True, decimal_places=7, max_digits=10)),
                ('longitud', models.DecimalField(blank=True, decimal_places=7, max_digits=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyecto_sst', to='detection.projects')),
            ],
            options={
                'verbose_name': 'Deteccion SST',
                'verbose_name_plural': 'Detecciones SST',
                'db_table': 'detections_sst',
            },
        ),
        migrations.CreateModel(
            name='DetectionSigns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_original', models.ImageField(blank=True, null=True, upload_to='original/signs')),
                ('imagen_procesada', models.ImageField(blank=True, null=True, upload_to='procesada/signs')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('descripcion', models.CharField(blank=True, max_length=255)),
                ('latitud', models.DecimalField(blank=True, decimal_places=7, max_digits=10)),
                ('longitud', models.DecimalField(blank=True, decimal_places=7, max_digits=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyecto_signs', to='detection.projects')),
                ('senal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detection_signs', to='detection.typesigns')),
            ],
            options={
                'verbose_name': 'Detección Señales',
                'verbose_name_plural': 'Detección Señales',
                'db_table': 'detections_signs',
            },
        ),
        migrations.CreateModel(
            name='DetectionMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_original', models.ImageField(blank=True, null=True, upload_to='original/materials')),
                ('imagen_procesada', models.ImageField(blank=True, null=True, upload_to='procesada/materials')),
                ('descripcion', models.CharField(blank=True, max_length=255)),
                ('latitud', models.DecimalField(blank=True, decimal_places=7, max_digits=10)),
                ('longitud', models.DecimalField(blank=True, decimal_places=7, max_digits=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyecto_materials', to='detection.projects')),
            ],
            options={
                'verbose_name': 'Detección Material',
                'verbose_name_plural': 'Detección Materiales',
                'db_table': 'detections_materials',
            },
        ),
        migrations.CreateModel(
            name='AuxSST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('deteccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detection', to='detection.sst')),
                ('deteccion_sst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detection_sst', to='detection.detectionsst')),
            ],
            options={
                'verbose_name': 'Aux SST',
                'verbose_name_plural': 'Aux SST',
                'db_table': 'aux_sst',
            },
        ),
        migrations.CreateModel(
            name='AuxSigns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('deteccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detection', to='detection.typesigns')),
                ('deteccion_signs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detection_sst', to='detection.detectionsigns')),
            ],
            options={
                'verbose_name': 'Aux Sing',
                'verbose_name_plural': 'Aux Sing',
                'db_table': 'aux_sing',
            },
        ),
        migrations.CreateModel(
            name='AuxMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('deteccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detection', to='detection.materials')),
                ('deteccion_materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detection_materials', to='detection.detectionmaterials')),
            ],
            options={
                'verbose_name': 'Aux Matertials',
                'verbose_name_plural': 'Aux Materials',
                'db_table': 'aux_materials',
            },
        ),
    ]
