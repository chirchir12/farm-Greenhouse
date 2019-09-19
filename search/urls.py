from django.urls import path
from .views import SearchProductListView


urlpatterns = [
    path('', SearchProductListView.as_view(), name='search')
]