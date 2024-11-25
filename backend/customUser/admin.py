from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)
admin.site.site_header = "Panneau d'administration Bat Opti"
admin.site.site_title = "Admin Bat Opti"
admin.site.index_title = "Bienvenue dans le panneau d'administration"
