from django.urls import path
from .views import homeView, detailShow

app_name = 'foodUrl'

urlpatterns = [
    path('', homeView, name='home'),
    path('<slug:theSLUG>',detailShow ),
]