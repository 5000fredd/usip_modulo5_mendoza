from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clases', views.ClasesViewSet)
router.register(r'maestros', views.MaestrosViewSet)
router.register(r'secciones', views.SeccionesViewSet)
router.register(r'estudiantes', views.EstudiantesViewSet)

urlpatterns = [
    #path('contact/<str:name>/', views.contact, name='contact'),
    #path('clases/', views.clases, name='clases'),
    #path('secciones/', views.seccionFormView, name='secciones'),
    #path('maestros/', views.maestroFormView, name='maestros'),
    #path('estudiantes/', views.estudianteFormView, name='estudiantes'),
    #path('', views.index),
    #path('', include(router.urls))
    path('clases/', views.ClaseCreateView.as_view()),
    path('clases/cantidad/', views.clase_count),
    path('maestros/', views.MaestroCreateView.as_view()),
    path('maestros/cantidad/', views.maestro_count),
    path('secciones/', views.SeccionCreateView.as_view()),
    path('estudiantes/', views.EstudianteCreateView.as_view()),
]
