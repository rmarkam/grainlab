# Generated by Django 2.0.3 on 2018-11-02 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_auto_20181102_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graintest',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
