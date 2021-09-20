from django.shortcuts import render
from .models import foodModels

def homeView(request):
    context = {
        'foods': foodModels.objects.all()
    }
    return render(request, 'index.html', context)
# Create your views here.
