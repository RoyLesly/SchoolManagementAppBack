# Generated by Django 5.0.1 on 2024-11-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincourse',
            name='course_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
