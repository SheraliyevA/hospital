# Generated by Django 5.0.3 on 2024-03-23 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klinika', '0016_rename_jami_tashxis_jami_narxi'),
    ]

    operations = [
        migrations.AddField(
            model_name='tashxis',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
