from django import forms
from .models import AdvUser, SubRubric
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import inlineformset_factory, Textarea
from captcha.fields import CaptchaField

from .apps import user_registered
from .models import Bb, AdditionalImage, Comment


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адресс электронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'send_messages')  # быстрое обьявление неизменных полей (стр 609)


class AdvUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = AdvUser
        fields = ('username', 'email')


class AdvUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True, label='Адресс электронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'send_messages')
        # fields = ('username', 'email', 'first_name', 'last_name',
        #           'send_messages','is_activated')


class RegisterUserForm(forms.ModelForm):  # форма реги 614 стр...
    # комбинируем быстрое и полное объявление полей
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')  # Полное объявление используем для создания полей электронной почты (поскольку хотим сделать его обязательным для заполнения)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())  # и обоих полей для занесения пароля
    password2 = forms.CharField(label='Повторите пароль ;)', widget=forms.PasswordInput,
                                help_text='Введите тот же самый пароль повторно для проверки')  # и обоих полей для занесения пароля

    def clean_password1(
            self):  # В методе clean _pas swordl () выполняем валидацию пароля, введенного в первое поле, с применением доступных в системе валидаторов пароля
        # Проверять таким же образом пароль из второго поля нет нужды - если пароль из первого поля некорректен, не имеет значения, является ли корректным пароль из второго поля.
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):  # В переопределенном методе clean () проверяем, совпадают ли оба введенных пароля.
        # Эта проверка будет проведена после валидации пароля из первого поля.
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):  # В переопределенном методе save ( )
        user = super().save(commit=False)  #
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False  # при сохранении нового пользователя заносим значения False в поля is_active
        user.is_activated = False  # e (признак, является ли пользователь активным)и is_activated (признак, выполнил ли пользователь процедуру активации),
        # тем самым сообщая фреймворку, что этот пользователь еще не может выполнять вход на сайт
        if commit:
            user.save()  # Далее сохраняем в записи закодированный пароль
        user_registered.send(RegisterUserForm,
                             instance=user)  # и отправляем сигнал _ regi stered, чтобы отослать пользователю письмо с требованием активации
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'send_messages')


class SubRubricForm(
    forms.ModelForm):  # У подрубрик сделаем поле надрубрики (super_ruЬric) обязательным для заполнения. Для этого мы объявим форму SuЬRuЬricFor
    super_rubric = forms.ModelChoiceField(queryset=SubRubric.object.all(), empty_label=None, label='Надрубрика',
                                          required=True)

    class Meta:
        model = SubRubric
        fields = '__all__'


class SearchForm(forms.Form): #Код формы поиска
    # искомое слово, введенное посетителем, будем пересылать  контроллеру методом GET в GЕТ-параметре keyword.
    keyword = forms.CharField(required=False, max_length=20, label='') # посетитель может ввести в поле keyword искомое слово, а может и не
    # ввести (чтобы отменить выполненный ранее поиск и вновь вывести все объявления из списка),мы пометили этj
    # поле как необязательное для заполнения. А еще убрали у этого поля надпись, присвоив параметру label пустую строку


class BbForm(forms.ModelForm): #Объявим форму , связанную с моделью Bb, для ввода самого объявления
    class Meta:
        model = Bb
        fields = '__all__'
        widgets = {'author': forms.HiddenInput , 'contacts': Textarea(attrs={'rows': 3})} # Hiddeninput, т. е. скрытое поле


AIFormSet = inlineformset_factory(Bb, AdditionalImage, fields='__all__') # встроенный набор форм AIFoпnSet,
# связанный с моделью Additional lrnage, в которые будут заноситься дополнительные иллюстрации


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('is_active',) # Поле is_act ive (признак, будет ли комментарий выводиться на странице) уберем из форм, поскольку оно требуется лишь администрации сайта
        widgets = {'bb': forms.HiddenInput} # У поля ьь, хранящего ключ объявления, с которым связан комментарий, укажем в качестве элемента управления скрытое поле.


class GuestCommentForm(forms.ModelForm):
    captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid': 'Неправильный текст'})

    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'bb': forms.HiddenInput}

