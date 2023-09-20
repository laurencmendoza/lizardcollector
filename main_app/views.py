from django.shortcuts import render
from .models import Lizard

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def lizards_index(request):
    lizards = Lizard.objects.all()
    return render(request, 'lizards/index.html', {
        'lizards': lizards
    })

def lizards_detail(request, lizard_id):
    lizard = Lizard.objects.get(id=lizard_id)
    return render(request, 'lizards/detail.html', {
        'lizard': lizard
    })