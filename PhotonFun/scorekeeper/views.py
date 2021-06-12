from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Match


def home(request):
    context = {
        'matches': Match.objects.all()
    }
    return render(request, 'scorekeeper/home.html', context)


class MatchListView(ListView):
    model = Match
    template_name = 'scorekeeper/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'matches'
    ordering = ['-match_datetime']
    paginate_by = 10


class PlayerMatchListView(ListView):
    model = Match
    template_name = 'scorekeeper/player_matches.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'matches'
    ordering = ['-match_datetime']
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Match.objects.filter(Q(player_a=user) | Q(player_b=user)).order_by('-match_datetime')


class MatchDetailView(DetailView):
    model = Match


class MatchCreateView(LoginRequiredMixin, CreateView):
    model = Match
    fields = ['player_a',
              'player_b',
              'points_a',
              'points_b',
              ]

    def form_valid(self, form):
        form.instance.referee = self.request.user
        return super().form_valid(form)


class MatchUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Match
    fields = ['referee',
              'player_a',
              'player_b',
              'points_a',
              'points_b',
              ]

    def form_valid(self, form):
        form.instance.referee = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.referee:
            return True
        return False


class MatchDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Match
    success_url = 'scorekeeper-home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.referee:
            return True
        return False


def about(request):
    return render(request, 'scorekeeper/about.html', {'title': 'About'})
