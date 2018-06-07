from django.conf.urls import url
from wineapp import views

app_name = 'wineapp'

urlpatterns = [
    url(r'^$',views.WineListView.as_view(),name='list'),
    url(r'(?P<pk>\d+)/$',views.WineDetailView.as_view(),name='detail'),
    url(r'^imports/(?P<pk>\d+)/$', views.ImporterDetailView.as_view(),name='import'),
    url(r'^distrib/(?P<pk>\d+)/$', views.DistributorDetailView.as_view(),name='distrib'),
    url(r'^ilist/',views.ImporterListView.as_view(),name='importers'),
    url(r'^dlist/',views.DistributorListView.as_view(),name='distributors'),


]
