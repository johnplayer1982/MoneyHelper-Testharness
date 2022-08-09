from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Tool

class HomeView(TemplateView):
    def get(self, request):
        template = 'shared/index.html'
        return render(request, template, {})

class StampDutyView(TemplateView):
    def get(self, request):
        template = 'tools/stamp_duty.html'
        return render(request, template, {})

class ToolList(ListView):
    model = Tool

class ToolDetail(DetailView):
    model = Tool
