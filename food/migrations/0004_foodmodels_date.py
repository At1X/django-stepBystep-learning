# Generated by Django 3.2.7 on 2021-09-20 15:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_foodmodels_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodmodels',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 20, 15, 53, 44, 606853, tzinfo=utc)),
        ),
    ]
