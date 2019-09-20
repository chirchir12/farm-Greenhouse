from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import FormMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Category, Product
from .forms import ContactForm


class ProductDetailView(FormMixin, DetailView):
    model = Product
    form_class = ContactForm
    template_name = 'products/detail.html'
    
    def get_success_url(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        return reverse_lazy('product-detail', kwargs={'slug':slug})

    def get_context_data(self, *args, **kwargs):

        context = super(ProductDetailView, self).get_context_data(
            *args, **kwargs)
        category = Category.objects.all().order_by('-timestamp')
        context['categories'] = category
        context['form'] = ContactForm
        return context


    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = get_object_or_404(Product, slug=slug)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("damn")
        # print(instance)
        if instance is None:
            raise Http404("hello product does not exists")
        return instance

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ProductDetailView, self).form_valid(form)


class ContactView(FormView):
    # form_class = ContactForm
    # success_url = reverse_lazy('product-detail')
    pass