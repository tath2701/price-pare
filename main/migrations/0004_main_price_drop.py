# Generated by Django 4.0.4 on 2022-06-16 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_main_options_remove_main_price_difference_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='price_drop',
            field=models.FloatField(default=0),
        ),
    ]
