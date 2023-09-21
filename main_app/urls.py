from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path('lizards/', views.lizards_index, name='index'),
    path('lizards/<int:lizard_id>/', views.lizards_detail, name='detail'),
    path('lizards/create/', views.LizardCreate.as_view(), name='lizards_create'),
    path('lizards/<int:pk>/update/', views.LizardUpdate.as_view(), name="lizards_update"),
    path('lizards/<int:pk>/delete/', views.LizardDelete.as_view(), name="lizards_delete"),
    path('lizards/<int:lizard_id>/add_feeding/', views.add_feeding, name='add_feeding')
]