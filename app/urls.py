from django.urls import path

from app.views import home

urlpatterns = [
    path("", home, name="home"),
    path("<slug:slug>/", home),
]
