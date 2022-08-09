from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Tool

class ToolList(ListView):
    model = Tool

class ToolDetail(DetailView):
    model = Tool
