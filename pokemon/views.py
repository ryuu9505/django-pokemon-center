from django.http import JsonResponse

POKEMON_DATA = [
    {'id': 1, 'name': 'Bulbasaur', 'type': 'Grass/Poison'},
    {'id': 2, 'name': 'Charmander', 'type': 'Fire'},
    {'id': 3, 'name': 'Squirtle', 'type': 'Water'},
]

def pokemon_list(request):
    return JsonResponse(POKEMON_DATA, safe=False)