from django.urls import path
from .views import (
    MatchListView,
    MatchDetailView,
    MatchCreateView,
    MatchUpdateView,
    MatchDeleteView,
    PlayerMatchListView
)
from . import views


urlpatterns = [
    path('', MatchListView.as_view(), name='scorekeeper-home'),
    path('user/<str:username>', PlayerMatchListView.as_view(), name='player-matches'),
    path('match/<int:pk>', MatchDetailView.as_view(), name='match-detail'),
    path('match/new/', MatchCreateView.as_view(), name='match-create'),
    path('match/<int:pk>/update/', MatchUpdateView.as_view(), name='match-update'),
    path('match/<int:pk>/delete/', MatchDeleteView.as_view(), name='match-delete'),
    path('about/', views.about, name='scorekeeper-about'),
]
