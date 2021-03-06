# Generated by Django 3.0.7 on 2020-07-23 19:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb_app', '0011_auto_20200705_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistrations',
            name='year',
            field=models.CharField(default='TY', max_length=2),
        ),
        migrations.AlterField(
            model_name='events',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 24, 1, 14, 18, 752420), help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
    ]
