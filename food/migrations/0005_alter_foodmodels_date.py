# Generated by Django 3.2.7 on 2021-09-20 15:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_foodmodels_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodmodels',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
