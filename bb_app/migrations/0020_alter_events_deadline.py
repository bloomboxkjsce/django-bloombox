# Generated by Django 3.2 on 2021-07-06 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb_app', '0019_alter_events_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 6, 21, 43, 40, 958177), help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
    ]
