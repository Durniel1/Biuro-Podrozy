# Generated by Django 5.0.4 on 2024-04-22 18:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_bilet_godzina_do_bilet_godzina_z'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilet',
            name='dodatkowe_oplaty',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='bilet',
            name='nr_siedzenia',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
