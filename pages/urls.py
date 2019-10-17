
from django.urls import path
from pages import views

urlpatterns = [
    path('home', views.IdexView.as_view(), name='index'),
    path('', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('categories/<slug:slug>', views.CategoryDetailView.as_view(), name='products'),
]