# Generated by Django 4.2.13 on 2024-06-08 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0003_rename_tipo_typesigns_nombre_remove_typesigns_codigo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sst',
            name='codigo',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
