# Generated by Django 3.2.11 on 2022-04-19 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionalimage',
            options={'verbose_name': 'Дополнительная иллюстрация', 'verbose_name_plural': 'Дополнительные иллюстрации'},
        ),
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-created_at'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='additionalimage',
            name='bb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletin_board.bb', verbose_name='Объявление'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='is_activated',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Прошел активацию?'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='send_messages',
            field=models.BooleanField(default=True, verbose_name='Слать оповещения о новых комментариях?'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор объявления'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='contacts',
            field=models.TextField(verbose_name='Контакты'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='bb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletin_board.bb', verbose_name='Объявление'),
        ),
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Название'),
        ),
    ]
