from django import forms
from .models import Solicitud_Servicio, Solicitud_Soporte

class Solicitud_ServicioModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control'
            f.field.widget.attrs['autocomplete'] = 'off'
            
    class Meta:
        model = Solicitud_Servicio
        fields = ['correo','telefono','descripcion']
        

class Solicitud_SoporteModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.visible_fields():
            f.field.widget.attrs['class'] = 'form-control'
            f.field.widget.attrs['autocomplete'] = 'off'
            
    class Meta:
        model = Solicitud_Soporte
        fields = ['correo','telefono','descripcion']
        widgets = {
            'telefono': forms.NumberInput(
                attrs={
                    'type': 'number',
                }
            ),
        }