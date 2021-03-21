from django.shortcuts import render
from django.viwes.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'app/index.html'
