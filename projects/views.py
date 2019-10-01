from django.shortcuts import render
from django.views.generic import ListView, View, DetailView, TemplateView
from .models import Project, ProjectDescription
from products.models import Category
from django.shortcuts import get_object_or_404


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/list.html'

    def get_context_data(self, *args, **kwargs):

        context = super(ProjectListView, self).get_context_data(
            *args, **kwargs)
        projectdes = ProjectDescription.objects.all().order_by('updated')[:1]
        projects = Project.objects.all()
        categories = Category.objects.all().order_by('priority')
        context['categories'] = categories
        context['project'] = True
        context['projects'] = projects
        context['projectdes'] = projectdes
        print(projectdes)
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail.html'

    def get_context_data(self, *args, **kwargs):

        context = super(ProjectDetailView, self).get_context_data(
            *args, **kwargs)
        slug = self.kwargs.get('slug')
    
        instance = get_object_or_404(Project, slug=slug)
        project_images = instance.otherimages.all()
        category = Category.objects.all()
        context['categories'] = category
        context['project_images'] = project_images
        return context

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
    
        instance = get_object_or_404(Project, slug=slug)
        
        return instance