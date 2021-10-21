from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import (
                                    MyShowObjectMixin,
                                    FormValid,
                                    ForbidAccess,
                                    DeleteAccess,
)
from django.views.generic import (
                                    ListView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
)

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

class MyUpdateView(LoginRequiredMixin,MyShowObjectMixin,FormValid,ForbidAccess, UpdateView):
    model = foodModels
    template_name = 'registration/create-update.html'

class AuthorDeleteView(DeleteAccess, DeleteView):
    model = foodModels
    success_url = reverse_lazy('account:home')
    template_name = 'registration/deleteView.html'
class ProfileView(UpdateView):
    model = User
    template_name = 'registration/profile.html'
    fields = ['username','first_name','last_name','email','vip_date']
    success_url = reverse_lazy('account:userProfile')
    def get_object(self, queryset=None):
        return User.objects.get(pk= self.request.user.pk)
