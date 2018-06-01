from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Wine(models.Model):
    name = models.CharField(max_length=256)
    producer = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    color = models.CharField(max_length=128)
    appellation = models.CharField(max_length=256)
    vintage = models.CharField(max_length=128)
    importer = models.ForeignKey('Importer',related_name='importers',null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wineapp:detail",kwargs={'pk':self.pk})

class Importer(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256,default=None)
    email = models.EmailField(default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wineapp:detail",kwargs={'pk':self.pk})
