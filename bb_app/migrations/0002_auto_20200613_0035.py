# Generated by Django 3.0.2 on 2020-06-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/campus-company/cc-logos'),
        ),
    ]
