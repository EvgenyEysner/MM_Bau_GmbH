from django.shortcuts import render
from django.views.generic import TemplateView, View, DetailView
# from .models import Navigation


class IndexView(TemplateView):
    template_name = 'app/index.html'
