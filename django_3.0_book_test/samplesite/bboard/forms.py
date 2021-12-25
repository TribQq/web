from django.forms import ModelForm
from .models import Bb


class BbForm(ModelForm):
    # класс производный от встроенного в жангу модуля ModelForm
    class Meta:
        model = Bb # класс модели с которой связанна форма
        fields = ('title','content','price','rubric') # поля формы
