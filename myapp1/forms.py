from django import forms
from myapp1.models import Experiencia, Aprendiz, Mentor, Actividad, NivelDeAprendizaje

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['nombre', 'descripcion', 'fecha', 'ubicacion', 'duracion', 'camada']
        widgets = {
            'nombre': forms.Select(choices=Experiencia.TIPOS_DE_EXPERIENCIA, attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 3}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ubicación'}),
            'duracion': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'camada': forms.NumberInput(attrs={'class': 'form-control'}),
        }

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
        widgets ={
            'experiencia': forms.Select(choices=[
                ('basico', 'Básico'),
                ('intermedio', 'Intermedío'),
                ('experto', 'Expertó')

            ])
        }

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre', 'fecha_de_entrega', 'nivel', 'experiencia', 'aprendiz']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'fecha_de_entrega': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nivel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nivel'}),
            'experiencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experiencia'}),
            'aprendiz': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aprendiz'}),
        }

class NivelDeAprendizajeForm(forms.ModelForm):
    class Meta:
        model = NivelDeAprendizaje
        fields = ['nombre', 'descripcion', 'activo']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }