from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog),
    path('blog_details', views.blog_details)

]
