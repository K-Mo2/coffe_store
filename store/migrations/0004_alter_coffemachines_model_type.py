# Generated by Django 4.0.2 on 2022-02-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_coffepods_pack_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffemachines',
            name='model_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
