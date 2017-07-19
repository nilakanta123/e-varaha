from django.contrib import admin

from .models import Viral, Bacterial, Genetic, NonInfectious, Parasitic, VitaminMinerals

admin.site.register(Viral)
admin.site.register(Bacterial)
admin.site.register(Genetic)
admin.site.register(NonInfectious)
admin.site.register(Parasitic)
admin.site.register(VitaminMinerals)
