# Generated by Django 4.0.4 on 2022-06-13 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_updated_date_main_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='main',
            options={},
        ),
        migrations.RemoveField(
            model_name='main',
            name='price_difference',
        ),
        migrations.AddField(
            model_name='main',
            name='logo_url',
            field=models.CharField(blank=True, max_length=220),
        ),
        migrations.AlterField(
            model_name='main',
            name='url',
            field=models.URLField(blank=True, max_length=220),
        ),
    ]
