# Generated by Django 2.0.3 on 2018-11-02 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_auto_20181102_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='graintest',
            name='infestation_days',
            field=models.IntegerField(default=16),
        ),
    ]
