# Generated by Django 4.2.7 on 2023-11-23 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_remove_profile_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='level',
        ),
    ]
