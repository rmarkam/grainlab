# Generated by Django 2.0.3 on 2018-11-02 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_graintest_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graintest',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]