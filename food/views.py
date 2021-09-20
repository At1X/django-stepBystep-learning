from django.shortcuts import render
from .models import foodModels
from django.core.paginator import Paginator

def homeView(request):
    ArticleList = foodModels.objects.show()
    paginator = Paginator(ArticleList, 3)
    page = request.GET.get('page')
    pageCONT = paginator.get_page(page)
    context = {
        'foods': pageCONT
    }
    return render(request, 'index.html', context)
def detailShow(request, theSLUG):
    context = {
        'details': foodModels.objects.get(slug=theSLUG)
    }
    return render(request, 'details.html', context)

# Create your views here.
