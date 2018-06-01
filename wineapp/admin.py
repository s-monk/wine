from django.contrib import admin
from wineapp.models import Wine
from wineapp.models import Importer
from wineapp.models import Distributor

# Register your models here.
admin.site.register(Wine)
admin.site.register(Importer)
admin.site.register(Distributor)
