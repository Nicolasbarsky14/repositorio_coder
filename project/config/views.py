from django.http import HttpResponse
from random import randint

def saludo(request):
    return HttpResponse ('hola')

def mi_nombre(request):
    nombre = input(f"cual es su nombre:" )
    return HttpResponse(f"Buenos dias {nombre}")

def nombre(request,nombre,apellido):
    return HttpResponse(f"{nombre}, {apellido}")

def fecha_hora(request):
    from datetime import datetime
    ahora = datetime.now().strftime(r"%d/%m/%Y %H:%M:%S.%f")
    return HttpResponse(ahora)

def tirar_dado(request):
    import random
    numero = random.randint(1,6)
    if numero == 6:
        return HttpResponse(f"Felicitaciones, has tirado el dado {numero}")
    else:
       return HttpResponse(f"Has tirado el dado numero {numero}, intente de nuevo")
