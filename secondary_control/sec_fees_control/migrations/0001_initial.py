# Generated by Django 5.0.1 on 2024-08-11 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivationKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, unique=True)),
                ('is_used', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Activation',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='SecSchoolFees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_charges', models.IntegerField(default=1000)),
                ('platform_paid', models.BooleanField(default=False)),
                ('balance', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Sec School Fees',
                'ordering': ('-balance',),
            },
        ),
        migrations.CreateModel(
            name='SecTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('BANK', 'BANK'), ('MTN', 'MTN'), ('ORANGE', 'ORANGE'), ('DIRECT', 'DIRECT')], max_length=255)),
                ('reason', models.CharField(choices=[('TUITION', 'TUITION'), ('REGISTRATION', 'REGISTRATION'), ('SCHOLARSHIP', 'SCHOLARSHIP'), ('PLATFORM CHARGES', 'PLATFORM CHARGES')], max_length=255)),
                ('ref', models.CharField(blank=True, max_length=35, null=True)),
                ('amount', models.IntegerField()),
                ('telephone', models.IntegerField(blank=True, null=True)),
                ('payer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(default='Pending', max_length=255)),
                ('operator', models.CharField(blank=True, choices=[('MTN', 'MTN'), ('ORANGE', 'ORANGE')], max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Sec Transactions',
                'ordering': ('-created_at',),
            },
        ),
    ]
