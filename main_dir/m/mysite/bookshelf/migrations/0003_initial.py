# Generated by Django 3.2.11 on 2022-03-20 15:30

import bookshelf.utilities
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookshelf', '0002_auto_20220320_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Book', max_length=10, verbose_name='Title')),
                ('subtitle', models.CharField(default='Name', max_length=15, verbose_name='Subtitle')),
                ('desc_title', models.CharField(blank=True, max_length=10, null=True, verbose_name='Title description')),
                ('desc_subtitle', models.CharField(blank=True, max_length=15, null=True, verbose_name='Subtitle description')),
                ('desc_text', models.TextField(default='Lorem ispum description', max_length=300, verbose_name='Description')),
                ('cover_img', models.ImageField(blank=True, null=True, upload_to=bookshelf.utilities.get_timestamp_path, verbose_name='Image on book cover')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='BookPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=bookshelf.utilities.get_timestamp_path, verbose_name='Page image')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.book')),
            ],
        ),
        migrations.CreateModel(
            name='BookProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.book')),
                ('book_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.bookpage')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.book')),
            ],
        ),
        migrations.CreateModel(
            name='ProgressCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.item')),
                ('condition_item_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.bookpage')),
            ],
        ),
        migrations.CreateModel(
            name='WinCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.book')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.progresscondition')),
                ('progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.bookprogress')),
            ],
        ),
        migrations.CreateModel(
            name='ProgressSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_time', models.DateTimeField(auto_now=True)),
                ('book_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.bookpage')),
                ('inventory_items', models.ManyToManyField(blank=True, to='bookshelf.Item')),
                ('progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.bookprogress')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('text', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pinned', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.book')),
                ('book_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookshelf.bookpage')),
            ],
        ),
        migrations.CreateModel(
            name='LoseCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.book')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.progresscondition')),
                ('progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.bookprogress')),
            ],
        ),
        migrations.CreateModel(
            name='DroppedItemSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.bookpage')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.item')),
                ('progress_save', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.progresssave')),
            ],
        ),
        migrations.CreateModel(
            name='DroppedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.bookpage')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.item')),
                ('progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.bookprogress')),
            ],
        ),
        migrations.AddField(
            model_name='bookprogress',
            name='inventory_items',
            field=models.ManyToManyField(blank=True, to='bookshelf.Item'),
        ),
        migrations.AddField(
            model_name='bookprogress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookpage',
            name='page_items',
            field=models.ManyToManyField(blank=True, to='bookshelf.Item'),
        ),
        migrations.AddField(
            model_name='book',
            name='first_page',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_page', to='bookshelf.bookpage', verbose_name='Start stage'),
        ),
        migrations.CreateModel(
            name='PageLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_path', models.CharField(blank=True, max_length=50, null=True)),
                ('from_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.bookpage')),
                ('key_items', models.ManyToManyField(blank=True, to='bookshelf.Item')),
                ('to_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_page', to='bookshelf.bookpage')),
            ],
            options={
                'unique_together': {('from_page', 'to_page')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='bookprogress',
            unique_together={('user', 'book')},
        ),
    ]
