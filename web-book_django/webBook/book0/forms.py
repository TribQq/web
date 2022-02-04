from django import forms

from .models import Book


class ImageForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'cover_img')