# Сериализация — процесс перевода структуры данных в последовательность байтов.

from rest_framework import serializers
from main.models import Bb,Comment


class BbSerializer(serializers.ModelSerializer): # , формирует список объявлений
    class Meta:
        model = Bb
        fields = ('id', 'title', 'content', 'price', 'created_at')


class BbDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = ('id', 'title', 'content', 'price', 'created_at', 'contacts', 'image') # В состав сведений о выбранном объявлении, помимо ключа записи, названия, описания,
        # цены товара и даты создания объявления, следует включить контакты и интернет-адрес основной иллюстрации.


class CommentSerializer(serializers.ModelSerializer): # Код сериализатора commentseriali zer, который будет отправлять список комментариев и добавлять новый комментарий,
    class Meta:
        model = Comment
        fields = ('bb', 'author', 'content', 'created_at')
