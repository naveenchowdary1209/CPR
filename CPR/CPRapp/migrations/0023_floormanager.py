# Generated by Django 3.0 on 2021-05-09 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPRapp', '0022_auto_20210508_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloorManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fmname', models.CharField(max_length=200)),
                ('floorno', models.CharField(max_length=200)),
                ('fcno', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
