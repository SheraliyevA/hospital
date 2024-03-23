# Generated by Django 5.0.3 on 2024-03-21 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klinika', '0002_rename_licheniya_tashxis_lecheniya'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bemor',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='bemor',
            name='dad_name',
        ),
        migrations.RemoveField(
            model_name='bemor',
            name='date',
        ),
        migrations.RemoveField(
            model_name='bemor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='bemor',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='bemor',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tashxis',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tashxis',
            name='date',
        ),
        migrations.RemoveField(
            model_name='tashxis',
            name='lecheniya',
        ),
        migrations.RemoveField(
            model_name='tashxis',
            name='narx',
        ),
        migrations.RemoveField(
            model_name='tashxis',
            name='tashxis',
        ),
        migrations.RemoveField(
            model_name='tashxis',
            name='tuladi',
        ),
        migrations.RemoveField(
            model_name='tashxis',
            name='user',
        ),
        migrations.AddField(
            model_name='bemor',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2024, 3, 21, 7, 47, 29, 414148, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='bemor',
            name='familiya',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bemor',
            name='ism',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bemor',
            name='otasining_ismi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bemor',
            name='yosh',
            field=models.IntegerField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tashxis',
            name='jami_narxi',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='tashxis',
            name='licheniya',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tashxis',
            name='tolagan_narxi',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='bemor',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bemor',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]