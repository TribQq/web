# Generated by Django 3.2.11 on 2022-02-09 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20220209_0913'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
    ]