# Generated by Django 4.2.5 on 2023-12-04 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0003_remove_userprofile_about_remove_userprofile_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='matricle',
            field=models.CharField(blank=True, default='2023-12-04 07:31:17.72738937', max_length=15),
        ),
    ]
