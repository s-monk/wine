from django.contrib import admin
from wineapp.models import Wine
from wineapp.models import Importer

# Register your models here.
admin.site.register(Wine)
admin.site.register(Importer)
