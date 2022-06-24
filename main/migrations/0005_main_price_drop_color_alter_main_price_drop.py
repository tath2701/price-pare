# Generated by Django 4.0.4 on 2022-06-16 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_main_price_drop'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='price_drop_color',
            field=models.CharField(default='gray', max_length=50),
        ),
        migrations.AlterField(
            model_name='main',
            name='price_drop',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=220),
        ),
    ]
