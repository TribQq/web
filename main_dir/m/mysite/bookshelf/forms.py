from django import forms
from django.forms import Form

from .models import Book, BookPage, Note


class NoteForm(forms.ModelForm):
    
    required_css_class = "form1_subtitle"
    error_css_class = "error"
    book_page = forms.ModelChoiceField(queryset=BookPage.objects.all())
    pinned = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class":"note_pin_checkbox" ,'id': 'pin_checkbox'}))
    
    
    class Meta:
        model = Note
        fields = ('title', 'text', 'book_page', 'pinned')
        widgets = {
            'title': forms.TextInput(attrs={'cols': 10, 'rows': 1, 'class': 'fields_contact_me'}),
            'text': forms.Textarea(attrs={'cols': 30, 'rows': 3, 'class': 'note_text'}),

        }




class ChangeNoteForm(forms.ModelForm): #форма из модели
    class Meta:
        model = Note
        fields =['text','pinned'] # field from model to form
        widgets = { #cutomize
            'text': forms.Textarea(attrs={'cols': 30, 'rows': 3})
        }
