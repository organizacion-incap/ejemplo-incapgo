from django.shortcuts import render

# Create your views here.
import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)



class Home(TemplateView):
    template_name = "index.html"
