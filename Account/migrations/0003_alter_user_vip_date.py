# Generated by Django 3.2.7 on 2021-10-18 11:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20211018_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='vip_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
