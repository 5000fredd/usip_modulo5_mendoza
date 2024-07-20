from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Clase, Maestro, Seccion, Estudiante
from .form import MaestroForm, SeccionForm, EstudianteForm 
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import ClaseSerializer, MaestroSerializer, SeccionSerializer, EstudianteSerializer
from rest_framework import generics
from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    return HttpResponse("Hola Mundo como va todo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de hoy")

def clases(request):
    post_nombre = request.POST.get("nombre")
    if post_nombre:
        q = Clase(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        clases = Clase.objects.filter(nombre__contains=filtro_nombre)
    else:
        clases = Clase.objects.all()
        
    return render(request, "form_clases.html", {"clases": clases})


def maestroFormView(request):
    form = MaestroForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "form_maestros.html", {"form": form}) 

def seccionFormView(request):
    form = SeccionForm()
    seccion = None
    id_seccion = request.GET.get("id")
    if id_seccion:
        #seccion = Seccion.objects.get(id=id_seccion)
        seccion= get_object_or_404(Seccion, id=id_seccion)
        form = SeccionForm(instance=seccion)
    
    if request.method == "POST":
        if seccion:
            form = SeccionForm(request.POST, instance=seccion)
        else:
            form = SeccionForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "form_secciones.html", {"form": form}) 

def estudianteFormView(request):
    form = EstudianteForm()
    estudiante = None
    id_estudiante = request.GET.get("id")
    if id_estudiante:
        #seccion = Seccion.objects.get(id=id_seccion)
        estudiante= get_object_or_404(Estudiante, id=id_estudiante)
        form = EstudianteForm(instance=estudiante)
    
    if request.method == "POST":
        if estudiante:
            form = EstudianteForm(request.POST, instance=estudiante)
        else:
            form = EstudianteForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "form_estudiantes.html", {"form": form}) 

class ClasesViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

class ClaseCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

class MaestrosViewSet(viewsets.ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer

class MaestroCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer

class SeccionesViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer

class SeccionCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer

class EstudiantesViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class EstudianteCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

@api_view(['GET'])
def clase_count(request):
    """
    Cuenta la cantidad de __clases__
    """

    try:
        cantidad = Clase.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )

@api_view(['GET'])
def maestro_count(request):
    """
    Cuenta la cantidad de __maestros__
    """

    try:
        cantidad = Maestro.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )
    
