# Generated by Django 3.2.5 on 2021-08-03 13:34

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0005_auto_20210610_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='analysis_reports',
        ),
        migrations.RemoveField(
            model_name='job',
            name='runtime_configuration',
        ),
        migrations.AddField(
            model_name='job',
            name='connectors_to_execute',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, default=list, size=None),
        ),
    ]