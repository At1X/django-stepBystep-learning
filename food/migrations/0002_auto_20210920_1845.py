# Generated by Django 3.2.7 on 2021-09-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodmodels',
            options={'verbose_name': 'غذا', 'verbose_name_plural': 'غذاها'},
        ),
        migrations.AlterField(
            model_name='foodmodels',
            name='rate',
            field=models.CharField(choices=[('3', 'Very good'), ('2', 'Good'), ('1', 'Bad')], max_length=1),
        ),
    ]
