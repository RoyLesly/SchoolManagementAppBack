# Generated by Django 4.2.5 on 2023-12-20 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordtoken',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='passwordtoken',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='passwordtoken_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]