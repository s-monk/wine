from django.conf.urls import url
from wineapp import views

app_name = 'wineapp'

urlpatterns = [
    url(r'^$',views.WineListView.as_view(),name='list'),
    url(r'(?P<pk>\d+)/$',views.WineDetailView.as_view(),name='detail'),
    url(r'(?P<pk>\d+)/$', views.ImporterDetailView.as_view(),name='detail'),
    url(r'^ilist/',views.ImporterListView.as_view(),name='ilist'),
]
