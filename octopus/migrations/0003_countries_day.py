# Generated by Django 3.2.5 on 2021-10-22 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('octopus', '0002_user_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('country_short', models.CharField(max_length=10)),
                ('country_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
            ],
        ),
    ]
