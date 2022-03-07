# Generated by Django 4.0.2 on 2022-03-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_coffemachines_options_alter_coffepods_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeBeans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('pack_size', models.CharField(choices=[('1', 'Small'), ('2', 'Medium'), ('3', 'Large')], max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Coffe Beans',
            },
        ),
    ]