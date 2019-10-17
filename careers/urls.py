from django.urls import path
from .views import career_view
from config import views



urlpatterns = [
    path('',career_view, name='careers' )
]