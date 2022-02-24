from django import forms
from .models import Note


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('name', 'text', 'book_page', 'pinned')
        widgets = {
            'name': forms.Textarea(attrs={'cols':10, 'rows':1}),
            'text': forms.Textarea(attrs={'cols': 30, 'rows': 3})
        }