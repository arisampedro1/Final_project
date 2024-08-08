from django import forms
from myapp1.models import Experiencia, Aprendiz, Mentor, Actividad, NivelDeAprendizaje

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['nombre', 'camada']
        widgets = {'nombre': forms.Select(choices=Experiencia.TIPOS_DE_EXPERIENCIA),}

class AprendizForm(forms.ModelForm):
    class Meta:
        model = Aprendiz
        fields = ['nombre', 'apellido', 'email', 'experiencia', 'nivel']
        widgets = {
            'nivel': forms.Select(choices=Aprendiz.NIVELES_DE_APRENDIZAJE),
        }

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['nombre', 'apellido', 'email', 'experiencia']

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre', 'fecha_de_entrega', 'nivel', 'experiencia', 'aprendiz']

class NivelDeAprendizajeForm(forms.ModelForm):
    class Meta:
        model = NivelDeAprendizaje
        fields = ['nombre']
