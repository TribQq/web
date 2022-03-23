# Generated by Django 3.2.11 on 2022-03-22 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0010_auto_20220322_1902'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProgressConditionItem',
            new_name='ProgressConditionStatusItem',
        ),
        migrations.RenameField(
            model_name='bookprogress',
            old_name='win_status',
            new_name='end_status',
        ),
        migrations.RemoveField(
            model_name='progresscondition',
            name='items',
        ),
        migrations.AddField(
            model_name='progresscondition',
            name='status_items',
            field=models.ManyToManyField(to='bookshelf.ProgressConditionStatusItem'),
        ),
    ]
