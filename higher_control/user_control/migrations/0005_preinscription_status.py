# Generated by Django 5.0.1 on 2024-09-23 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0004_preinscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='preinscription',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('VERIFIED', 'VERIFIED')], default='PENDING', max_length=8),
            preserve_default=False,
        ),
    ]
