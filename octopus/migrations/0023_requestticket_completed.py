# Generated by Django 3.2.5 on 2021-10-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('octopus', '0022_foodbank_building_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestticket',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
