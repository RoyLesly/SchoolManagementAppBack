# Generated by Django 5.0.1 on 2024-08-24 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='matricle',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
