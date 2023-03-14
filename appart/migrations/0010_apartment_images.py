# Generated by Django 4.1.7 on 2023-03-13 10:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appart', '0009_remove_apartment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to='apartment_images'), default=list, size=None),
        ),
    ]