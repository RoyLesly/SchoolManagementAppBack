# Generated by Django 5.0.1 on 2024-09-04 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees_control', '0006_transactions_operation_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='account',
            field=models.CharField(default='REGISTRATION', max_length=50),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='reason',
            field=models.CharField(default='Edit', max_length=255),
        ),
    ]
