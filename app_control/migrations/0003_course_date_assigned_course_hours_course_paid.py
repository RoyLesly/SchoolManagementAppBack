# Generated by Django 4.2.5 on 2023-12-20 04:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_assigned',
            field=models.DateField(default=datetime.datetime(2023, 12, 20, 5, 47, 21, 900981)),
        ),
        migrations.AddField(
            model_name='course',
            name='hours',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]