from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import MyShowObjectMixin,FormValid
from django.views.generic import ListView, CreateView
from food.models import foodModels
# from .models import User
@login_required()
def home(request):
    return render(request, 'registration/home.html')
# Create your views here.

class TheHome(LoginRequiredMixin, ListView):
    def get_queryset(self):
        if self.request.user.is_superuser:
            return foodModels.objects.all()
        else:
            return foodModels.objects.filter(user=self.request.user)
    template_name = 'registration/home.html'
class MyCreateView(LoginRequiredMixin,MyShowObjectMixin,FormValid, CreateView):
    model = foodModels
    template_name = 'registration/create-update.html'
