from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def lizards_index(request):
    return render(request, 'lizards/index.html', {
        'lizards': lizards
    })

lizards = [
    {'name': 'DJ Crazy Tongue', 'species': 'Blue-tongued skink', 'description': 'clever and hungry', 'age': 1},
    {'name': 'Lizzie', 'species': 'Mexican mole lizard', 'description': 'the sweetest girl', 'age': 3},
    {'name': 'Kurt', 'species': 'Komodo dragon', 'description': 'large and in charge', 'age': 15},
]