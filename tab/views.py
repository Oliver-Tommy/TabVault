from django.shortcuts import render
from django.views import generic
from .models import Tab

# Create your views here.

class TabList(generic.ListView):
    model = Tab
    template_name = "tab/index.html"
    paginate_by = 6