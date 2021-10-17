from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from food.models import foodModels
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
class MyCreateView(LoginRequiredMixin, CreateView):
    model = foodModels
    fields = ['user','name','slug','desc','rate','auth','date','categ', 'img','check',]
    template_name = 'registration/create-update.html'
