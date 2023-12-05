from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_control', '0001_initial'),
        ('app_control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialty',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialty_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='specialty',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='specialty_level', to='app_control.level'),
        ),
        migrations.AddField(
            model_name='specialty',
            name='main_specialty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='specialty_main_specialty', to='app_control.mainspecialty'),
        ),
        migrations.AddField(
            model_name='specialty',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialty_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='result',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='result_course', to='app_control.course'),
        ),
        migrations.AddField(
            model_name='result',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='result_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='result',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='result_userprofile', to='user_control.userprofile'),
        ),
        migrations.AddField(
            model_name='result',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='result_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mainspecialty',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_specialty_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mainspecialty',
            name='domain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialty_domain', to='app_control.domain'),
        ),
        migrations.AddField(
            model_name='mainspecialty',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_specialty_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='maincourse',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_course_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='maincourse',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_course_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='level',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='level_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='level',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='level_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='domain',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='domain_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='domain',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='domain_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_lecturer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='main_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='course_main_course', to='app_control.maincourse'),
        ),
        migrations.AddField(
            model_name='course',
            name='specialty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='course_specialty', to='app_control.specialty'),
        ),
        migrations.AddField(
            model_name='course',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='specialty',
            constraint=models.UniqueConstraint(fields=('main_specialty', 'academic_year', 'level'), name='unique_specialty'),
        ),
        migrations.AddConstraint(
            model_name='result',
            constraint=models.UniqueConstraint(fields=('course', 'student'), name='unique_result'),
        ),
        migrations.AddConstraint(
            model_name='course',
            constraint=models.UniqueConstraint(fields=('specialty', 'main_course'), name='unique_course'),
        ),
    ]
