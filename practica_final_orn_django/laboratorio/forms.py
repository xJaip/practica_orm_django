from django import forms
from .models import Laboratorio

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'pais', 'ciudad']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)