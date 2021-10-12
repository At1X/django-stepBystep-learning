from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from food.models import foodModels
@login_required()
def home(request):
    return render(request, 'registration/home.html')
# Create your views here.

class TheHome(LoginRequiredMixin, ListView):
    model = foodModels
    template_name = 'registration/home.html'
