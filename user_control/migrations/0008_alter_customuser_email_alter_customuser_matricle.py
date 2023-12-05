# Generated by Django 4.2.5 on 2023-12-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0007_alter_customuser_email_alter_customuser_matricle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='matricle',
            field=models.CharField(blank=True, default=43378, max_length=15),
        ),
    ]