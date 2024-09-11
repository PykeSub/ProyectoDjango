from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def renderTemplate(request):
    return render(request, 'templatesApp/index.html')   

def pagina2(request):
    data = {'nombre' : 'paul',
            'apellido' : 'alvarez'}
    return render(request, 'templatesApp/pagina2.html', data)

def infoUsuario(request):
    data = {'ID' : '123',
            'Nombre' : 'Clark Kent',
            'Email' : 'superman@jl.org'}
    return render(request, 'templatesApp/userInfoTemplate.html', data)