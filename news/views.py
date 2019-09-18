from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView, DetailView
from .models import Post
from products.models import Category


class POSTListView(ListView):
    model = Post
    template_name = "posts/list.html"

    
    def get_context_data(self,*args, **kwargs):
        context = super(POSTListView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        context['post'] = True
        return context
    




class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"

    
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Post, slug=slug)
        return instance
    
