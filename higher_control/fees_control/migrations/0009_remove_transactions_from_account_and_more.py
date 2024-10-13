# Generated by Django 5.0.1 on 2024-09-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees_control', '0008_transactions_from_account_transactions_to_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='from_account',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='to_account',
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
