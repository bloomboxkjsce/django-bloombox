# Generated by Django 3.0.7 on 2020-06-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb_app', '0007_delete_partners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistrations',
            name='contact',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eventregistrationshackathon',
            name='leaderContact',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='contact',
            field=models.CharField(max_length=15),
        ),
    ]
