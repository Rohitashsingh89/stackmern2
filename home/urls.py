from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('base1/', views.base1),
    path('services/', views.services),
    path('services_details/', views.services_details),
    path('login/', views.login),
    path('register/', views.register),
    path('contact/', views.contact),
    path('about/', views.about),
    path('team/', views.team)

]
