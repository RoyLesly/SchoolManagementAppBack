# Generated by Django 5.0.1 on 2024-09-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees_control', '0009_remove_transactions_from_account_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='from_account',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='to_account',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
    ]
