# Generated by Django 5.0.3 on 2024-03-22 03:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klinika', '0007_tashxis_tashxis_alter_bemor_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bemor',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2024, 3, 22, 3, 21, 0, 101946, tzinfo=datetime.timezone.utc)),
        ),
    ]
