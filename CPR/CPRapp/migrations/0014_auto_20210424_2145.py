# Generated by Django 3.0 on 2021-04-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPRapp', '0013_auto_20210424_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='improfile',
            name='aadharno',
            field=models.CharField(default=10, max_length=16),
        ),
        migrations.AddField(
            model_name='improfile',
            name='contactno',
            field=models.CharField(default=10, max_length=10),
        ),
    ]
