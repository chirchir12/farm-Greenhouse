from django.urls import path
from .views import ProjectListView, ProjectDetailView


urlpatterns = [
    path('',ProjectListView.as_view(), name='projects' ),
     path('<slug:slug>',ProjectDetailView.as_view(), name='project-detail' )
]