# Generated by Django 3.2.7 on 2021-09-23 10:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('start_data', models.DateTimeField()),
                ('end_data', models.DateTimeField()),
                ('limit', models.IntegerField(default=0)),
                ('used', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]