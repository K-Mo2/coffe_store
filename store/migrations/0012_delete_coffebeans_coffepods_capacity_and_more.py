# Generated by Django 4.0.2 on 2022-03-06 15:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_coffebeans_pack_size'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CoffeBeans',
        ),
        migrations.AddField(
            model_name='coffepods',
            name='capacity',
            field=models.FloatField(default=1000, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='coffepods',
            name='quantity',
            field=models.PositiveIntegerField(default=1000),
        ),
    ]
