from django.shortcuts import render
from .models import Match


def home(request):
    context = {
        'matches': Match.objects.all()
    }
    return render(request, 'scorekeeper/home.html', context)


def about(request):
    return render(request, 'scorekeeper/about.html', {'title': 'About'})
