# Generated by Django 4.2.5 on 2023-12-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0006_alter_course_date_assigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('I', 'I'), ('II', 'II')], default='I', max_length=15),
        ),
    ]