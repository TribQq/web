# Generated by Django 3.2.11 on 2022-02-19 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book0', '0026_auto_20220218_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookprogress',
            name='dropped_item',
        ),
    ]