
from django.urls import path
from .views import  ProductDetailView, ContactView

urlpatterns = [
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('contact/', ProductDetailView.as_view(), name='contact')
   
]
