from django.urls import path
from .views import career_view
urlpatterns = [
    path('',career_view, name='careers' )
]