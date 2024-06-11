# Generated by Django 4.2.13 on 2024-06-08 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detectionsigns',
            options={'verbose_name': 'Detección Señales', 'verbose_name_plural': 'Detección Señales'},
        ),
        migrations.RemoveField(
            model_name='projects',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='longitud',
        ),
        migrations.AddField(
            model_name='detectionmaterials',
            name='latitud',
            field=models.DecimalField(blank=True, decimal_places=7, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detectionmaterials',
            name='longitud',
            field=models.DecimalField(blank=True, decimal_places=7, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detectionsigns',
            name='latitud',
            field=models.DecimalField(blank=True, decimal_places=7, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detectionsigns',
            name='longitud',
            field=models.DecimalField(blank=True, decimal_places=7, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detectionsst',
            name='latitud',
            field=models.DecimalField(blank=True, decimal_places=7, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detectionsst',
            name='longitud',
            field=models.DecimalField(blank=True, decimal_places=7, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
