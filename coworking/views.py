from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def inicio(request):
    nombre_plataforma = "CoworkSpace"
    descripcion = "Plataforma para gestionar espacios de coworking."

    mensaje = f"""
    <h1>Bienvenido a {nombre_plataforma}</h1>
    <p>{descripcion}</p>
    <p>Encuentra, consulta y reserva espacios de coworking.</p>
    """

    return HttpResponse(mensaje)