# Generated by Django 4.0.2 on 2022-02-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_coffemachines_model_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffemachines',
            name='model_type',
            field=models.CharField(blank=True, choices=[('1', 'base model'), ('2', 'premium model'), ('3', 'deluxe model')], max_length=50, null=True),
        ),
    ]
