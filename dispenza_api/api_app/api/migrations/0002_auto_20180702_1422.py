# Generated by Django 2.0.6 on 2018-07-02 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spesa',
            name='prezzo_tot',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='prezzo spesa', max_digits=6, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]
