# Generated by Django 4.0.4 on 2022-06-16 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_main_current_price_alter_main_previous_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='current_price',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
