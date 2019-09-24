from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView, View, DetailView, TemplateView
from products.models import Category
from products.forms import ContactForm
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy



class IdexView(ListView):
    model = Category
    template_name = 'pages/index.html'
    def get_context_data(self, *args, **kwargs):

        context = super(IdexView, self).get_context_data(
            *args, **kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context



class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, *args, **kwargs):

        context = super(AboutPageView, self).get_context_data(
            *args, **kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        context['about'] = True
        return context


class ContactPageView(FormMixin, TemplateView):
    template_name = 'pages/contact.html'
    form_class = ContactForm

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('contact')

    def get_context_data(self, *args, **kwargs):

        context = super(ContactPageView, self).get_context_data(
            *args, **kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        context['contact'] = True
        context['form'] = ContactForm
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ContactPageView, self).form_valid(form)


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
        instance = get_object_or_404(Category, slug=slug)
        products = instance.product_set.all().order_by('timestamp')
        return products
