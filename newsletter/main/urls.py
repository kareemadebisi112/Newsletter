from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendToDatabase/', views.sendToDatabase, name='sendToDatabase')
]