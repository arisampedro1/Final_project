# myapp1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Vistas para Experiencia
    path('', views.inicio, name='Inicio'),
    path('experiencias/', views.experiencia_list, name='experiencia_list'),
    path('experiencia/<int:pk>/', views.experiencia_detail, name='experiencia_detail'),
    path('experiencia/crear/', views.experiencia_create, name='experiencia_create'),
    path('experiencia/<int:pk>/editar/', views.experiencia_update, name='experiencia_update'),
    path('experiencia/<int:pk>/eliminar/', views.experiencia_delete, name='experiencia_delete'),

    # Vistas para Aprendiz
    path('aprendices/', views.aprendiz_list, name='aprendiz_list'),
    path('aprendiz/<int:pk>/', views.aprendiz_detail, name='aprendiz_detail'),
    path('aprendiz/crear/', views.aprendiz_create, name='aprendiz_create'),
    path('aprendiz/<int:pk>/editar/', views.aprendiz_update, name='aprendiz_update'),
    path('aprendiz/<int:pk>/eliminar/', views.aprendiz_delete, name='aprendiz_delete'),

    # Vistas para Mentor
    path('mentores/', views.mentor_list, name='mentor_list'),
    path('mentor/<int:pk>/', views.mentor_detail, name='mentor_detail'),
    path('mentor/crear/', views.mentor_create, name='mentor_create'),
    path('mentor/<int:pk>/editar/', views.mentor_update, name='mentor_update'),
    path('mentor/<int:pk>/eliminar/', views.mentor_delete, name='mentor_delete'),

    # Vistas para Actividad
    path('actividades/', views.actividad_list, name='actividad_list'),
    path('actividad/<int:pk>/', views.actividad_detail, name='actividad_detail'),
    path('actividad/crear/', views.actividad_create, name='actividad_create'),
    path('actividad/<int:pk>/editar/', views.actividad_update, name='actividad_update'),
    path('actividad/<int:pk>/eliminar/', views.actividad_delete, name='actividad_delete'),

    # Vistas para NivelDeAprendizaje
    path('niveles/', views.nivel_list, name='nivel_list'),
    path('nivel/<int:pk>/', views.nivel_detail, name='nivel_detail'),
    path('nivel/crear/', views.nivel_create, name='nivel_create'),
    path('nivel/<int:pk>/editar/', views.nivel_update, name='nivel_update'),
    path('nivel/<int:pk>/eliminar/', views.nivel_delete, name='nivel_delete'),
]
