# Generated by Django 5.0 on 2023-12-26 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0013_review_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='rental/cars/images'),
        ),
    ]
