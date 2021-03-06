# Generated by Django 3.0.7 on 2021-03-19 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb_app', '0016_auto_20210318_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esummitregistration',
            name='year',
            field=models.CharField(default='TY', max_length=20),
        ),
        migrations.AlterField(
            model_name='events',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 20, 0, 56, 47, 547059), help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
    ]
