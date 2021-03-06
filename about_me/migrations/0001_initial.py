# Generated by Django 3.2.11 on 2022-04-19 11:59

import about_me.utilities
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioProjectCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_img', models.ImageField(blank=True, null=True, upload_to=about_me.utilities.get_timestamp_path, verbose_name='Project logo img')),
                ('cover_img', models.ImageField(upload_to=about_me.utilities.get_timestamp_path, verbose_name='Project cover img')),
                ('project_type', models.CharField(max_length=15)),
                ('web_version_link', models.TextField(blank=True, max_length=100, null=True)),
                ('git_link', models.TextField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioSkillCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('border_color', models.TextField(choices=[('#38c695', 'green'), ('#fc5f45', 'red'), ('#b27cf5', 'purple'), ('#feb960', 'orange')], verbose_name='color')),
                ('cover_img', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
    ]
