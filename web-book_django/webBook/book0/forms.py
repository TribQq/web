from django import forms

from .models import Book,Note


class ImageForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'cover_img')

#формочку с докой
class ChangeNoteForm(forms.ModelForm): #форма из модели
    class Meta:
        model = Note
        fields =['text','pinned'] # field from model to form
        widgets = { #cutomize
            'text': forms.Textarea(attrs={'cols': 30, 'rows': 3})
        }


class TestForm(forms.Form): #просто форма
    your_name = forms.CharField(label='Your name', max_length=5)
    # text = forms.TextInput()
    name = forms.Field(label='name')