from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MusicYearbookView(TemplateView):
    template_name = 'music_yearbook/index.html'