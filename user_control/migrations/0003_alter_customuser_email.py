# Generated by Django 4.2.5 on 2023-12-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0002_remove_passwordtoken_user_profile_passwordtoken_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
