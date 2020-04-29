from django.contrib import admin
from .models import Stoppage, Bus, Next

# Register your models here.
admin.site.register(Stoppage)
admin.site.register(Bus)
admin.site.register(Next)