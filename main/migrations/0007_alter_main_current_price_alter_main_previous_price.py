# Generated by Django 4.0.4 on 2022-06-16 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_main_price_drop_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='current_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AlterField(
            model_name='main',
            name='previous_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
    ]
