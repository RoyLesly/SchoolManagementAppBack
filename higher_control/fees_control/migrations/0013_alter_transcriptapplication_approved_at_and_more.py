# Generated by Django 5.0.1 on 2024-09-23 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees_control', '0012_transactions_origin_transcriptapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcriptapplication',
            name='approved_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transcriptapplication',
            name='printed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
