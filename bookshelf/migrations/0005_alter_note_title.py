# Generated by Django 3.2.11 on 2022-04-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0004_remove_bookprogress_inventory_full'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.TextField(max_length=20),
        ),
    ]