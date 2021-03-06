# Generated by Django 3.2.5 on 2021-10-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('octopus', '0009_auto_20211023_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodbank',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodbank',
            name='phone_number',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
