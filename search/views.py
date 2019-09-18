from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product, Category


class SearchProductListView(ListView):
    template_name = "search/view.html"
    paginate_by = 12

    
    def get_context_data(self, **kwargs):
        context = super(SearchProductListView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories']=categories
        return context
    

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)
        print(query)
        if query is not None:
            lookup = Q(title__icontains=query) | Q(description__icontains=query)
            qs=Product.objects.filter(lookup).distinct()
            print(qs)
            if qs.exists():
                return qs

            else:
                return Product.objects.all()
        return Product.objects.all()




