# class MyShowObjectMixin():
#     def dispatch(self, request, *args, **kwargs):
#         if not self.request.user.is_superuser:
#             self.fields = ['user', 'name', 'slug', 'desc', 'rate', 'auth', 'date', 'categ', 'img', 'check' ]
#         else:
#             self.fields = [ 'name', 'slug', 'desc', 'rate', 'categ', 'img',]
#         return super().dispatch(request, *args, **kwargs)
