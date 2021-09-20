from django.shortcuts import render
from .models import foodModels, Category
from django.core.paginator import Paginator

def homeView(request):
    ArticleList = foodModels.objects.show()
    paginator = Paginator(ArticleList, 3)
    page = request.GET.get('page')
    pageCONT = paginator.get_page(page)
    context = {
        'foods': pageCONT,
        'cat': Category.objects.all()
    }
    return render(request, 'index.html', context)
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
