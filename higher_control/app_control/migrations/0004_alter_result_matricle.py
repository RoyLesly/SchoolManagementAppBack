# Generated by Django 5.0.1 on 2024-08-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0003_result_matricle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='matricle',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
