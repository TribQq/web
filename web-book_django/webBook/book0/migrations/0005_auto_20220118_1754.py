# Generated by Django 3.2.11 on 2022-01-18 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book0', '0004_pagelink_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagelink',
            name='from_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frommaterial', to='book0.bookpage'),
        ),
        migrations.AlterField(
            model_name='pagelink',
            name='to_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tomaterial', to='book0.bookpage'),
        ),
    ]
