# Generated by Django 2.0.3 on 2018-11-02 00:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrainTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(default=uuid.uuid4, max_length=255)),
                ('grain_type', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('supplier_name', models.CharField(max_length=255)),
                ('supplier_country', models.CharField(max_length=255)),
                ('supplier_region', models.CharField(max_length=255)),
                ('supplier_city', models.CharField(max_length=255)),
                ('supplier_zip', models.CharField(max_length=255)),
                ('buyer_name', models.CharField(max_length=255)),
                ('buyer_country', models.CharField(max_length=255)),
                ('buyer_region', models.CharField(max_length=255)),
                ('buyer_city', models.CharField(max_length=255)),
                ('buyer_zip', models.CharField(max_length=255)),
                ('notes', models.TextField(max_length=255)),
                ('sample_image', models.ImageField(upload_to='')),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
