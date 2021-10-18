from django.shortcuts import render, get_object_or_404
from .models import foodModels, Category
from Account.models import User
from django.core.paginator import Paginator
from django.views import generic
#
# def homeView(request):
#     ArticleList = foodModels.objects.show()
#     paginator = Paginator(ArticleList, 3)
#     page = request.GET.get('page')
#     pageCONT = paginator.get_page(page)
#     context = {
#         'foods': pageCONT,
#     }
#     return render(request, 'index.html', context)
class base(generic.ListView):
    template_name = 'index.html'
    queryset = foodModels.objects.show()
    paginate_by = 3
    context_object_name = 'foods'

    # kinda ListView, easier one.

# class base(ListView):
#     model = foodModels
#     paginate_by = 3
    # end


# def detailShow(request, theSLUG):
#     context = {
#         'details': foodModels.objects.get(slug=theSLUG)
#     }
#     return render(request, 'details.html', context)

class DetDetailView(generic.DetailView):
    template_name = 'details.html'
    def get_object(self):
        slug = self.kwargs.get('theSLUG')
        return get_object_or_404(foodModels.objects.show(), slug=slug)
        

# def categoryShow(request, categID):
#     context = {
#         'catp': Category.objects.get(slug=categID)
#     }
#     return render(request, 'category.html', context)

class CategoryShow(generic.ListView):
    template_name = 'category.html'
    paginate_by = 3
    def get_queryset(self):
        global categories
        slug = self.kwargs.get('categID')
        categories = get_object_or_404(Category, slug=slug)
        return foodModels.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catp'] = categories
        return context

class AuthorShow(generic.ListView):
    template_name = 'author_list.html'
    paginate_by = 3
    def get_queryset(self):
        global user
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        return User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = user
        return context

