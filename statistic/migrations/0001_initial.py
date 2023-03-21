# Generated by Django 4.1.7 on 2023-03-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(unique=True, verbose_name='Date')),
                ('unique_users', models.IntegerField(blank=True, null=True, verbose_name='Unique Users')),
                ('users_start', models.IntegerField(blank=True, null=True, verbose_name='Command Start')),
                ('users_finsh', models.IntegerField(blank=True, null=True, verbose_name='Communication with an agent')),
                ('users_pay', models.IntegerField(blank=True, null=True, verbose_name='Made a payment')),
            ],
        ),
    ]
