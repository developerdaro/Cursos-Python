from django.shortcuts import render
from .models import Usuario
# Create your views here.
def listarUsuarios(request):
    consulta=Usuario.objects.all()
    return render(request,'listarusuario.html',{'consulta':consulta})
