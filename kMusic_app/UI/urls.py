from django.urls import path
from .views import CatListViews
from . import views

urlpatterns = [
	path("", views.cover, name = "home"),
	path('ui/', views.ui, name= "ui"),
	path('cat/', CatListViews.as_view(), name="catalog")
]
