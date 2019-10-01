from django.shortcuts import render
from .forms import CareerForm
from products.models import Category

from .models import JobDescription



def career_view(request):
    categories = Category.objects.all()
    JobDescriptionList = JobDescription.objects.filter(display=True)
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
        'careers':careers,
        'jobs':JobDescriptionList
    }
    return render(request, 'careers/career.html', context)

