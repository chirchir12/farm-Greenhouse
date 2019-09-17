from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView, View, DetailView, TemplateView
from products.models import Category


class IdexView(ListView):
    model = Category
    template_name = 'pages/index.html'
    def get_context_data(self, *args, **kwargs):

        context = super(IdexView, self).get_context_data(
            *args, **kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class CategoryDetailView(DetailView):
    template_name = "pages/category-service.html"

    def get_context_data(self, *args, **kwargs):

        context = super(CategoryDetailView, self).get_context_data(
            *args, **kwargs)
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Category, slug=slug)
        products = instance.product_set.all()
        categories = Category.objects.all()
        category_instance = get_object_or_404(Category, slug=slug)
        context['categories'] = categories
        context['products'] = products
        context['category_instance'] = category_instance
        return context

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')

        try:
            instance = get_object_or_404(Category, slug=slug)
            products = instance.product_set.all()
        except Category.DoesNotExist:
            raise Http404('Does not Exist')
        return products
