from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.listContent, name='list'),
    path('passage', views.getPassage, name='passage'),
]