# Generated by Django 5.0.1 on 2024-11-20 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preinscription',
            name='program',
            field=models.CharField(choices=[('HND', 'HND'), ('BTS', 'BTS'), ('AQP', 'AQP'), ('BSC', 'BSC'), ('B-TECH', 'B-TECH'), ('M-TECH', 'M-TECH'), ('PHD', 'PHD'), ('LICENSE', 'LICENSE'), ('MASTERS', 'MASTERS'), ('DPQ', 'DPQ'), ('OND', 'OND'), ('B-ENG', 'B-ENG'), ('B-ENG', 'B-ENG'), ('CISCO', 'CISCO')], max_length=12),
        ),
    ]
