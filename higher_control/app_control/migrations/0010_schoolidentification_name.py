# Generated by Django 5.0.1 on 2024-09-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0009_schoolinfo_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolidentification',
            name='name',
            field=models.CharField(default='', max_length=80),
        ),
    ]
