# Generated by Django 3.2.9 on 2022-01-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_bb_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='contacts',
            field=models.TextField(verbose_name='Контакты'),
        ),
    ]
