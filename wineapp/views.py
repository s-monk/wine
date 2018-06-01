from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View, TemplateView, ListView,
                                  DetailView, CreateView, UpdateView,
                                  DeleteView)
from wineapp import models

class IndexView(TemplateView):
    template_name = 'index.html'

class WineListView(ListView):
    context_object_name = 'wines'
    model = models.Wine

class WineDetailView(DetailView):
    context_object_name = "wine_detail"
    model = models.Wine
    template_name = "wineapp/wine_detail.html"

class ImporterListView(ListView):
    context_object_name = "importers"
    model = models.Importer

class ImporterDetailView(DetailView):
    context_object_name = 'importer_detail'
    model = models.Importer
    template_name = "wineapp/importer_detail.html"

class DistributorListView(ListView):
    context_object_name = 'distributors'
    model = models.Distributor

class DistributorDetailView(DeleteView):
    context_object_name = 'distributor_detail'
    model = models.Distributor
    template_name = "wineapp/distributor.html"
# Create your views here.
