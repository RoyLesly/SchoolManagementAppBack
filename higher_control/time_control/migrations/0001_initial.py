# Generated by Django 5.0.1 on 2024-11-28 14:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_control', '0011_rename_campus_campushigher_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTableDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('day', models.CharField(choices=[('MONDAY', 'MONDAY'), ('TUESDAY', 'TUESDAY'), ('WEDNESDAY', 'WEDNESDAY'), ('THURSDAY', 'THURSDAY'), ('FRIDAY', 'FRIDAY'), ('SATURDAY', 'SATURDAY'), ('SUNDAY', 'SUNDAY')], max_length=15)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='timetableday_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('CHECKED-IN', 'CHECKED-IN'), ('CHECKED-OUT', 'CHECKED-OUT'), ('NOT-CHECKED-IN', 'NOT-CHECKED-IN'), ('OUT-BY-SYSTEM', 'OUT-BY-SYSTEM')], default='I', max_length=15)),
                ('action', models.CharField(choices=[('PENDING', 'PENDING'), ('IN', 'IN'), ('OUT', 'OUT'), ('OUT-BY-SYSTEM', 'OUT-BY-SYSTEM')], default='PENDING', max_length=15)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('hours', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('session', models.CharField(choices=[('Morning', 'Morning'), ('Evening', 'Evening')], default='Morning', max_length=15)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timeslot_course', to='app_control.course')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='timeslot_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='timeslot_updated_by', to=settings.AUTH_USER_MODEL)),
                ('timetableday', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='time_control.timetableday')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTableWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_week', models.CharField(max_length=7)),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='timetableweek_created_by', to=settings.AUTH_USER_MODEL)),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_control.specialty')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='timetableweek_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='timetableday',
            name='timetableweek',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='time_control.timetableweek'),
        ),
        migrations.AddConstraint(
            model_name='timeslot',
            constraint=models.UniqueConstraint(fields=('start', 'timetableday'), name='unique_timeslot'),
        ),
        migrations.AddConstraint(
            model_name='timetableweek',
            constraint=models.UniqueConstraint(fields=('specialty', 'year_week'), name='unique_timetableweek'),
        ),
        migrations.AddConstraint(
            model_name='timetableday',
            constraint=models.UniqueConstraint(fields=('day', 'timetableweek'), name='unique_timetableday'),
        ),
    ]
