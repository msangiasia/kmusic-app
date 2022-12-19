from django.shortcuts import render
from django.views.generic import ListView
from .models import Catalog

# Create your views here.

def cover(request):
	return render(request, 'cover.html')

def index(request):
	return render(request, "home/index.html")

def ui(request):
	return render(request, "ui/registration.html")

class CatListViews(ListView):
	model = Catalog
	template_name = "utility/404.html"
