# Generated by Django 5.0.3 on 2024-03-22 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klinika', '0011_alter_bemor_date_created_alter_tashxis_vaqt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tashxis',
            name='bemor',
        ),
        migrations.DeleteModel(
            name='Bemor',
        ),
        migrations.DeleteModel(
            name='Tashxis',
        ),
    ]
