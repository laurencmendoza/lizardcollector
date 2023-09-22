from django.contrib import admin
from .models import Lizard, Feeding, Food

# Register your models here.
admin.site.register(Lizard)
admin.site.register(Feeding)
admin.site.register(Food)
