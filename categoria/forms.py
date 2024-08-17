from django import forms
from .models import Categoria


class CategoriaModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control'
            f.field.widget.attrs['autocomplete'] = 'off'
            
    class Meta:
        model = Categoria
        fields = ['titulo','imagen','sistemas']