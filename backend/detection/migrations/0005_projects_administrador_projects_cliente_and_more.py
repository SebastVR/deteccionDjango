# Generated by Django 4.2.13 on 2024-06-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0004_sst_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='administrador',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='projects',
            name='cliente',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='projects',
            name='estado',
            field=models.CharField(blank=True, choices=[('Activo', 'Activo'), ('En liquidación', 'En liquidación'), ('Inactivo', 'Inactivo'), ('Suspendido', 'Suspendido'), ('Terminado', 'Terminado')], default='Activo', max_length=255),
        ),
        migrations.AlterField(
            model_name='projects',
            name='codigo',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='sst',
            name='codigo',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='sst',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]