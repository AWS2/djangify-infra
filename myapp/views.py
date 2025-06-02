import socket
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def host_info(request):
    hostname = socket.gethostname()
    return HttpResponse(f"Hola! Estás viendo la respuesta desde el contenedor: {hostname}")
