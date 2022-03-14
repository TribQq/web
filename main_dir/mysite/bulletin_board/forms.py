from django import forms

from .models import AdvUser


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='E-mail address') # обязательное поле

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name', 'send_messages')
