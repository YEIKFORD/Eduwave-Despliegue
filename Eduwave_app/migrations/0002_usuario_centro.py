# Generated by Django 5.1.3 on 2025-04-15 20:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eduwave_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='centro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Eduwave_app.centroformacion'),
            preserve_default=False,
        ),
    ]
