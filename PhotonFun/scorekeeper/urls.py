from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='scorekeeper-home'),
    path('about/', views.about, name='scorekeeper-about'),
]
