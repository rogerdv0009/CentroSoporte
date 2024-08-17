from django import forms
from .models import Noticia



class NoticiaModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control'
            f.field.widget.attrs['autocomplete'] = 'off'
            
    class Meta:
        model = Noticia
        fields = ['titulo','imagen','resumen','descripcion','fecha']
        widgets = {
            'fecha': forms.DateInput(
                attrs={
                    'placeholder': 'Fecha',
                    'type': 'date',
                }
            ),
        }