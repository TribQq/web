# Generated by Django 3.2.11 on 2022-02-19 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book0', '0027_remove_bookprogress_dropped_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DroppedItem',
        ),
    ]
