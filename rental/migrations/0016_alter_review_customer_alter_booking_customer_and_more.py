# Generated by Django 5.0 on 2023-12-27 20:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '__first__'),
        ('rental', '0015_remove_car_image_carimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.customer'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
