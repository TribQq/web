from .models import Tabli4ka
from django.forms import ModelForm, TextInput, Textarea


class Tabli4kaForm(ModelForm):
    class Meta: #доп настройки
        model = Tabli4ka #указываем модель с которой работаем
        fields = ['title', 'task'] # поля которые должны присутсвовать
        widgets = {'title': TextInput(attrs = {
            'class' : 'form-control' ,
            'placeholder' : 'print name here'}),
            'task':Textarea(attrs = {
            'class' : 'form-control' ,
            'placeholder' : 'print text here'})
        } #передаём обьектам(полям нужные свойства( которыже уже протестили на кастомных)
        # <input type="text" placeholder="print here name" class = 'form-control'><br>
        # <textarea placeholder="print here" class="form-control"></textarea><br>