# Generated by Django 4.2.5 on 2023-12-20 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0005_alter_course_date_assigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_assigned',
            field=models.DateField(blank=True, null=True),
        ),
    ]
