# Generated by Django 4.0.4 on 2022-06-16 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_main_current_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='current_price',
            field=models.FloatField(default=-1),
        ),
        migrations.AlterField(
            model_name='main',
            name='previous_price',
            field=models.FloatField(default=-1),
        ),
        migrations.AlterField(
            model_name='main',
            name='price_change',
            field=models.FloatField(default=-1),
        ),
    ]
