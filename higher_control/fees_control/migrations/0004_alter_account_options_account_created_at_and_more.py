# Generated by Django 5.0.1 on 2024-08-30 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees_control', '0003_account'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ('-created_at',), 'verbose_name_plural': 'Accounts'},
        ),
        migrations.AddField(
            model_name='account',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2024, 8, 30, 12, 36, 52, 129349)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(choices=[('REGISTRATION', 'REGISTRATION'), ('TUITION', 'TUITION'), ('SCHOLARSHIP', 'SCHOLARSHIP')], max_length=255, unique=True),
        ),
    ]
