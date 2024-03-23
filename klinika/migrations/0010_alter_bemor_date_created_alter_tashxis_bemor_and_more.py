# Generated by Django 5.0.3 on 2024-03-22 04:15

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klinika', '0009_tashxis_vaqt_alter_bemor_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bemor',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2024, 3, 22, 4, 15, 33, 591644, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='tashxis',
            name='bemor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bemori', to='klinika.bemor'),
        ),
        migrations.AlterField(
            model_name='tashxis',
            name='vaqt',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 4, 15, 33, 592644, tzinfo=datetime.timezone.utc)),
        ),
    ]