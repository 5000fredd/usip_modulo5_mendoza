from django import forms
from .models import Maestro, Seccion, Estudiante


class SeccionForm(forms.ModelForm):
    class Meta:
        model = Seccion
        fields = '__all__'

class MaestroForm(forms.ModelForm):
    class Meta:
        model = Maestro
        fields = '__all__'
        
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'