#from django.shortcuts import render
# pages/views.py
# Create your views here.

from django.views.generic import TemplateView


class HomePageView(TemplateView):
	template_name = 'home.html'
