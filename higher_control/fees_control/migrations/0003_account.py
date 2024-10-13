# Generated by Django 5.0.1 on 2024-08-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees_control', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('REGISTRATION', 'REGISTRATION'), ('TUITION', 'TUITION'), ('SCHOLARSHIP', 'SCHOLARSHIP'), ('OTHERS', 'OTHERS')], max_length=255, unique=True)),
                ('number', models.CharField(blank=True, max_length=35, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
