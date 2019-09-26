from django.shortcuts import render
from .forms import CareerForm
from products.models import Category


def career_view(request):
    categories = Category.objects.all()
    careers = True
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CareerForm()

    else:
        form = CareerForm()

    context = {
        'form':form,
        'categories':categories,
        'careers':careers
    }
    return render(request, 'careers/career.html', context)

