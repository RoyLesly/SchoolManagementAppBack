# Generated by Django 5.0.1 on 2024-08-11 05:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fees_control', '0001_initial'),
        ('user_control', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='activationkey',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_method_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activationkey',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_method_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='schoolfees',
            name='userprofile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='schoolfees_userprofile', to='user_control.userprofile'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transaction_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transactions',
            name='schoolfees',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fees_control.schoolfees'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transaction_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
