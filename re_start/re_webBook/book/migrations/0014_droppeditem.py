# Generated by Django 3.2.11 on 2022-02-22 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_alter_progresssave_save_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='DroppedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookpage')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.item')),
                ('progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookprogress')),
            ],
        ),
    ]