# Generated by Django 3.2.11 on 2022-05-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0006_auto_20220419_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='progress_conditions',
            field=models.ManyToManyField(blank=True, null=True, to='bookshelf.ProgressCondition', verbose_name='lose/win conditions'),
        ),
    ]