# Generated by Django 2.2.3 on 2019-08-29 05:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0009_help'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='unit',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='message',
            new_name='notification',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='name',
        ),
        migrations.AddField(
            model_name='notification',
            name='of_type',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='notification',
            name='severity_level',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='notification',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
