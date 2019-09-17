from django.urls import path
from .views import POSTListView, PostDetailView
urlpatterns = [
    path('',POSTListView.as_view(), name='posts' ),
    path('<slug:slug>/',PostDetailView.as_view(), name='posts-detail' )
]