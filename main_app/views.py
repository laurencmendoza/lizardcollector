from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Lizard, Food
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    return render(request, 'lizards/detail.html', {
        'lizard': lizard, 
        'feeding_form': feeding_form
    })

class LizardCreate(CreateView):
    model = Lizard
    fields = '__all__'

class LizardUpdate(UpdateView):
    model = Lizard
    fields = '__all__'

class LizardDelete(DeleteView):
    model = Lizard
    success_url = '/lizards'

def add_feeding(request, lizard_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.lizard_id = lizard_id
        new_feeding.save()
    return redirect('detail', lizard_id=lizard_id)

class FoodList(ListView):
    model = Food

class FoodDetail(DetailView):
    model = Food

class FoodCreate(CreateView):
    model = Food
    fields = '__all__'

class FoodUpdate(UpdateView):
    model = Food
    fields = ['name', 'found_at']

class FoodDelete(DeleteView):
    model = Food
    success_url = '/foods'
