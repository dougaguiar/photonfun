from django.urls import path

from .views import PlayersListView, register

app_name = 'users'
urlpatterns = [
    path('register/', register, name='register'),
    path('players/', PlayersListView.as_view(), name='players-home')
]