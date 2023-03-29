from django.shortcuts import render
from RegistroPokemon.models import pokemon
def registro(request):
    if request.method == 'POST':
        Codigo = request.POST['codigo']
        Nombre = request.POST['nombre']
        Elemento = request.POST['elemento']
        Genero = request.POST['genero']
        Estado = request.POST['estado']

        pokemoncito = pokemon(codigo=Codigo, nombre=Nombre, elemento=Elemento, genero=Genero, estado=Estado)
        pokemoncito.save()

        return render(request, "DBPokemon.html", {"nombre": Nombre})
    return render(request, "DBPokemon.html")
