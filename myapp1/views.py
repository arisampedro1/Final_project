from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Experiencia, Aprendiz, Mentor, Actividad, NivelDeAprendizaje
from .forms import ExperienciaForm, AprendizForm, MentorForm, ActividadForm, NivelDeAprendizajeForm
from django.contrib.auth.decorators import login_required

# Vistas para Experiencia

def inicio(request):
    return render(request, 'myapp1/index.html')


@login_required
def experiencia_list(request):
    experiencias = Experiencia.objects.all()
    return render(request, 'myapp1/experiencia_list.html', {'experiencias': experiencias})

@login_required
def experiencia_detail(request, pk):
    try:
        experiencia = Experiencia.objects.get(pk=pk)
    except Experiencia.DoesNotExist:
        return HttpResponseNotFound("Experiencia no encontrada")
    return render(request, 'myapp1/experiencia_detail.html', {'experiencia': experiencia})

@login_required
def experiencia_create(request):
    if request.method == "POST":
        form = ExperienciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experiencia_list')
    else:
        form = ExperienciaForm()
    return render(request, 'myapp1/experiencia_form.html', {'form': form, 'title': 'Crear Experiencia'})

@login_required
def experiencia_update(request, pk):
    try:
        experiencia = Experiencia.objects.get(pk=pk)
    except Experiencia.DoesNotExist:
        return HttpResponseNotFound("Experiencia no encontrada")
    
    if request.method == "POST":
        form = ExperienciaForm(request.POST, instance=experiencia)
        if form.is_valid():
            form.save()
            return redirect('experiencia_list')
    else:
        form = ExperienciaForm(instance=experiencia)
    return render(request, 'myapp1/experiencia_form.html', {'form': form, 'title': 'Actualizar Experiencia'})

@login_required
def experiencia_delete(request, pk):
    try:
        experiencia = Experiencia.objects.get(pk=pk)
    except Experiencia.DoesNotExist:
        return HttpResponseNotFound("Experiencia no encontrada")
    
    if request.method == "POST":
        experiencia.delete()
        return redirect('experiencia_list')
    return render(request, 'myapp1/experiencia_confirm_delete.html', {'experiencia': experiencia})

# Vistas para Aprendiz
@login_required
def aprendiz_list(request):
    aprendices = Aprendiz.objects.all()
    return render(request, 'myapp1/aprendiz_list.html', {'aprendices': aprendices})

@login_required
def aprendiz_detail(request, pk):
    try:
        aprendiz = Aprendiz.objects.get(pk=pk)
    except Aprendiz.DoesNotExist:
        return HttpResponseNotFound("Aprendiz no encontrado")
    return render(request, 'aprendiz_detail.html', {'aprendiz': aprendiz})

@login_required
def aprendiz_create(request):
    if request.method == "POST":
        form = AprendizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aprendiz_list')
    else:
        form = AprendizForm()
    return render(request, 'myapp1/aprendiz_form.html', {'form': form, 'title': 'Crear Aprendiz'})

@login_required
def aprendiz_update(request, pk):
    try:
        aprendiz = Aprendiz.objects.get(pk=pk)
    except Aprendiz.DoesNotExist:
        return HttpResponseNotFound("Aprendiz no encontrado")
    
    if request.method == "POST":
        form = AprendizForm(request.POST, instance=aprendiz)
        if form.is_valid():
            form.save()
            return redirect('aprendiz_list')
    else:
        form = AprendizForm(instance=aprendiz)
    return render(request, 'myapp1/aprendiz_form.html', {'form': form, 'title': 'Actualizar Aprendiz'})

@login_required
def aprendiz_delete(request, pk):
    try:
        aprendiz = Aprendiz.objects.get(pk=pk)
    except Aprendiz.DoesNotExist:
        return HttpResponseNotFound("Aprendiz no encontrado")
    
    if request.method == "POST":
        aprendiz.delete()
        return redirect('aprendiz_list')
    return render(request, 'myapp1/aprendiz_confirm_delete.html', {'aprendiz': aprendiz})

# Vistas para Mentor
@login_required
def mentor_list(request):
    mentores = Mentor.objects.all()
    return render(request, 'myapp1/mentor_list.html', {'mentores': mentores})

@login_required
def mentor_detail(request, pk):
    try:
        mentor = Mentor.objects.get(pk=pk)
    except Mentor.DoesNotExist:
        return HttpResponseNotFound("Mentor no encontrado")
    return render(request, 'myapp1/mentor_detail.html', {'mentor': mentor})

@login_required
def mentor_create(request):
    if request.method == "POST":
        form = MentorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mentor_list')
    else:
        form = MentorForm()
    return render(request, 'myapp1/mentor_form.html', {'form': form, 'title': 'Crear Mentor'})

@login_required
def mentor_update(request, pk):
    try:
        mentor = Mentor.objects.get(pk=pk)
    except Mentor.DoesNotExist:
        return HttpResponseNotFound("Mentor no encontrado")
    
    if request.method == "POST":
        form = MentorForm(request.POST, instance=mentor)
        if form.is_valid():
            form.save()
            return redirect('mentor_list')
    else:
        form = MentorForm(instance=mentor)
    return render(request, 'myapp1/mentor_form.html', {'form': form, 'title': 'Actualizar Mentor'})

@login_required
def mentor_delete(request, pk):
    try:
        mentor = Mentor.objects.get(pk=pk)
    except Mentor.DoesNotExist:
        return HttpResponseNotFound("Mentor no encontrado")
    
    if request.method == "POST":
        mentor.delete()
        return redirect('mentor_list')
    return render(request, 'myapp1/mentor_confirm_delete.html', {'mentor': mentor})

# Vistas para Actividad
@login_required
def actividad_list(request):
    actividades = Actividad.objects.all()
    return render(request, 'myapp1/actividad_list.html', {'actividades': actividades})

@login_required
def actividad_detail(request, pk):
    try:
        actividad = Actividad.objects.get(pk=pk)
    except Actividad.DoesNotExist:
        return HttpResponseNotFound("Actividad no encontrada")
    return render(request, 'myapp1/actividad_detail.html', {'actividad': actividad})

@login_required
def actividad_create(request):
    if request.method == "POST":
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actividad_list')
    else:
        form = ActividadForm()
    return render(request, 'myapp1/actividad_form.html', {'form': form, 'title': 'Crear Actividad'})

@login_required
def actividad_update(request, pk):
    try:
        actividad = Actividad.objects.get(pk=pk)
    except Actividad.DoesNotExist:
        return HttpResponseNotFound("Actividad no encontrada")
    
    if request.method == "POST":
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('actividad_list')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'myapp1/actividad_form.html', {'form': form, 'title': 'Actualizar Actividad'})

@login_required
def actividad_delete(request, pk):
    try:
        actividad = Actividad.objects.get(pk=pk)
    except Actividad.DoesNotExist:
        return HttpResponseNotFound("Actividad no encontrada")
    
    if request.method == "POST":
        actividad.delete()
        return redirect('actividad_list')
    return render(request, 'myapp1/actividad_confirm_delete.html', {'actividad': actividad})

# Vistas para NivelDeAprendizaje
@login_required
def nivel_list(request):
    niveles = NivelDeAprendizaje.objects.all()
    return render(request, 'myapp1/nivel_list.html', {'niveles': niveles})

@login_required
def nivel_detail(request, pk):
    try:
        nivel = NivelDeAprendizaje.objects.get(pk=pk)
    except NivelDeAprendizaje.DoesNotExist:
        return HttpResponseNotFound("Nivel de Aprendizaje no encontrado")
    return render(request, 'myapp1/nivel_detail.html', {'nivel': nivel})

@login_required
def nivel_create(request):
    if request.method == "POST":
        form = NivelDeAprendizajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nivel_list')
    else:
        form = NivelDeAprendizajeForm()
    return render(request, 'myapp1/nivel_form.html', {'form': form, 'title': 'Crear Nivel de Aprendizaje'})

@login_required
def nivel_update(request, pk):
    try:
        nivel = NivelDeAprendizaje.objects.get(pk=pk)
    except NivelDeAprendizaje.DoesNotExist:
        return HttpResponseNotFound("Nivel de Aprendizaje no encontrado")
    
    if request.method == "POST":
        form = NivelDeAprendizajeForm(request.POST, instance=nivel)
        if form.is_valid():
            form.save()
            return redirect('nivel_list')
    else:
        form = NivelDeAprendizajeForm(instance=nivel)
    return render(request, 'myapp1/nivel_form.html', {'form': form, 'title': 'Actualizar Nivel de Aprendizaje'})

@login_required
def nivel_delete(request, pk):
    try:
        nivel = NivelDeAprendizaje.objects.get(pk=pk)
    except NivelDeAprendizaje.DoesNotExist:
        return HttpResponseNotFound("Nivel de Aprendizaje no encontrado")
    
    if request.method == "POST":
        nivel.delete()
        return redirect('nivel_list')
    return render(request, 'myapp1/nivel_confirm_delete.html', {'nivel': nivel})
