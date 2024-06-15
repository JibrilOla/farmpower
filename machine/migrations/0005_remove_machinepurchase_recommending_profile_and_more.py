# Generated by Django 4.2.7 on 2023-11-26 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0004_alter_machinepurchase_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machinepurchase',
            name='recommending_profile',
        ),
        migrations.RemoveField(
            model_name='machinepurchase',
            name='revenue',
        ),
        migrations.AlterField(
            model_name='machinepurchase',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 15, 10, 16, 471391, tzinfo=datetime.timezone.utc)),
        ),
    ]
