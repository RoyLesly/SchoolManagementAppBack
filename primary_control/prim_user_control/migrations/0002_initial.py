# Generated by Django 5.0.1 on 2024-10-30 08:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prim_user_control', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='primaryprofile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='primaryprofile_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='primaryprofile',
            constraint=models.UniqueConstraint(fields=('primary_classroom', 'user'), name='unique_primaryprofile'),
        ),
    ]
