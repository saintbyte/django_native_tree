from django.shortcuts import render


def home(request, slug=None):
    return render(request, "home/index.html", {})
