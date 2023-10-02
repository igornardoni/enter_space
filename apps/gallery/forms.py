from django import forms
from apps.gallery.models import Fotografia

class PhotographForm(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada', ]
        labels = {
            'descricao': 'Descrição',
            'data_inclusao': 'Data de registro',
            'usuario': 'Usuário',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_inclusao': forms.DateInput(
                format='%d/%m/%Y',
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'usuario': forms.Select(attrs={'class': 'form-control'})
        }


