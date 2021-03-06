# Generated by Django 3.2.6 on 2021-08-06 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODate', models.CharField(max_length=100)),
                ('AccountOpenDate', models.CharField(max_length=100)),
                ('CurBalance', models.CharField(max_length=100)),
                ('pbirthdate', models.CharField(max_length=100)),
                ('firstcity', models.CharField(max_length=100)),
                ('firstzippostal', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=100)),
            ],
        ),
    ]
