from django.shortcuts import render
from .models import foodModels, Category
from django.core.paginator import Paginator
from django.views.generic import ListView
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
class base(ListView):
    template_name = 'index.html'
    queryset = foodModels.objects.show()
    paginate_by = 3
    context_object_name = 'foods'

def detailShow(request, theSLUG):
    context = {
        'details': foodModels.objects.get(slug=theSLUG)
    }
    return render(request, 'details.html', context)
def categoryShow(request, categID):
    context = {
        'catp': Category.objects.get(slug=categID)
    }
    return render(request, 'category.html', context)
# Create your views here.
