from django.http import Http404
from django.utils import timezone
from food.models import foodModels
from django.shortcuts import render, get_object_or_404
class MyShowObjectMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            self.fields = ['user', 'name', 'slug', 'desc', 'rate', 'auth', 'date', 'categ', 'img', 'check' ]
        else:
            self.fields = [ 'name', 'slug', 'desc', 'rate', 'categ', 'img',]
        return super().dispatch(request, *args, **kwargs)
class FormValid():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.user = self.request.user
            self.obj.check = False
        return super().form_valid(form) #super().<function name>(args)

#ForbidAccess mixin use for forbid user to access other articles and edit them changing url pk
#and also forbid normal users to access published articles (even if they wrote them)
class ForbidAccess():
    def dispatch(self, request,pk, *args, **kwargs):
        articles = get_object_or_404(foodModels, pk=pk)
        if (articles.user == self.request.user)  and articles.check == False or (self.request.user.is_superuser):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('You havent access to this page')
