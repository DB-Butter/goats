from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Expertise, Goat, CustomGoat # import the Artist model from models.py
# Register your models here.

admin.site.register(Goat) # this line will add the model to the admin panel
admin.site.register(Expertise)
admin.site.register(CustomGoat)
