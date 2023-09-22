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
    path('lizards/<int:lizard_id>/add_feeding/', views.add_feeding, name='add_feeding'), 
    path('lizards/<int:lizard_id>/assoc_food/<int:food_id>/', views.assoc_food, name='assoc_food'), 
    path('lizards/<int:lizard_id>/unassoc_food/<int:food_id>/', views.unassoc_food, name='unassoc_food'), 
    path('foods/', views.FoodList.as_view(), name='foods_index'), 
    path('foods/<int:pk>/', views.FoodDetail.as_view(), name='foods_detail'), 
    path('foods/create/', views.FoodCreate.as_view(), name='foods_create'), 
    path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='foods_update'), 
    path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'), 
]