from django.utils import timezone
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
