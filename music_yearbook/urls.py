from django.contrib import admin
from django.urls import include, path

from . import views as site_views
from music_yearbook.views import MonthView
from music_yearbook import views as music_views

# namespace
app_name = "music_yearbook"
urlpatterns = [
    path("", music_views.MusicYearbookView.as_view(), name="index"),
    path("<int:year>/<int:month>/", MonthView.as_view(), name="month"),
]
