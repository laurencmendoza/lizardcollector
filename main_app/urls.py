from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path('lizards/', views.lizards_index, name='index'),
    path('lizards/<int:lizard_id>/', views.lizards_detail, name='detail'),
]