from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class HomePage(TemplateView):
    template_name = 'homepage.html'

class aboutview(TemplateView):
    template_name = 'about.html'