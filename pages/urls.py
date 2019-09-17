
from django.urls import path
from pages import views

urlpatterns = [
    path('', views.IdexView.as_view(), name='index'),
    path('categories/<slug:slug>', views.CategoryDetailView.as_view(), name='products'),
]