# Generated by Django 4.2.7 on 2023-11-25 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0002_alter_machinepurchase_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinepurchase',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 25, 21, 3, 45, 985988, tzinfo=datetime.timezone.utc)),
        ),
    ]
