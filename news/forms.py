from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'hashtag', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание новости'
            }),
            'hashtag': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Хештег без решетки. Например: Животные, Деньги, Жилье'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Полный текст вводить в это поле'
            }),
        }
