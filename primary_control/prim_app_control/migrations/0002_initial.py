# Generated by Django 5.0.1 on 2024-10-30 08:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_control', '0002_initial'),
        ('prim_app_control', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='primaryclassroom',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Primary_subject_lecturer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='primaryclassroom',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Primary_classroom_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='primaryclassroom',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Primary_classroom_school_info', to='app_control.schoolinfo'),
        ),
        migrations.AddField(
            model_name='primaryclassroom',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Primary_classroom_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='primarylevel',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Primary_level_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='primarylevel',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Primary_level_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='primaryclassroom',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classroom_level', to='prim_app_control.primarylevel'),
        ),
        migrations.AddField(
            model_name='primarymainsubject',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Primary_main_subject_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='primarymainsubject',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Primary_main_subject_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='primarysubject',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Primary_subject_class', to='prim_app_control.primaryclassroom'),
        ),
        migrations.AddField(
            model_name='primarysubject',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Primary_subject_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='primarysubject',
            name='main_subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Primary_subject_main_subject', to='prim_app_control.primarymainsubject'),
        ),
        migrations.AddField(
            model_name='primarysubject',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Primary_subject_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='primarylevel',
            constraint=models.UniqueConstraint(fields=('level',), name='unique_Primary_level'),
        ),
        migrations.AddConstraint(
            model_name='primaryclassroom',
            constraint=models.UniqueConstraint(fields=('school', 'level', 'academic_year'), name='unique_Primary_classroom'),
        ),
        migrations.AddConstraint(
            model_name='primarysubject',
            constraint=models.UniqueConstraint(fields=('classroom', 'main_subject'), name='unique_Primary_subject'),
        ),
    ]
