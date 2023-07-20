from django.shortcuts import render


usuarios = [
    {
        'nombre' : "Gabriel",
        'apellido' : "Muñoz",
        'direccion' : "Avenida 123",
        'correo' : "gabriel_2023@example.com",
    },
    {
        'nombre' : "Jimena",
        'apellido' : "Lopez",
        'direccion' : "Calle 28",
        'correo' : "jimena.lopez@example.com",
    },
    {
        'nombre' : "Laura",
        'apellido' : "Ramirez",
        'direccion' : "pasaje b-31",
        'correo' : "laura.ramirez@example.com",
    },
    {
        'nombre' : "Carlos",
        'apellido' : "Sanchez",
        'direccion' : "Calle 12",
        'correo' : "carlos.sanchez@example.com",
    },
    {
        'nombre' : "Pedro",
        'apellido' : "Gonzalez",
        'direccion' : "Carrera 45",
        'correo' : "pedro.gonzalez@example.com",
    },
]
# Create your views here.

def index(request):
    return render(request, 'app_landing_page/index.html')

def lista_usuarios(request):
    auxiliar = {
        'usuarios': usuarios
    }
    return render(request, 'app_landing_page/usuarios.html', auxiliar)