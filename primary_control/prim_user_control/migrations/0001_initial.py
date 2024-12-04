# Generated by Django 5.0.1 on 2024-10-30 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prim_app_control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('code', models.ImageField(blank=True, null=True, upload_to='code')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('primary_classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primaryprofile_classroom', to='prim_app_control.primaryclassroom')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
