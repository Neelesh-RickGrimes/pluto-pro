# Generated by Django 3.2.5 on 2021-10-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('octopus', '0014_auto_20211023_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestticket',
            name='note',
            field=models.TextField(max_length=1024, null=True),
        ),
    ]