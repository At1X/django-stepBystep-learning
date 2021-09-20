from django.urls import path
from .views import  detailShow, categoryShow, base

app_name = 'foodUrl'

urlpatterns = [
    path('',base.as_view() , name='home'),
    path('<slug:theSLUG>',detailShow ),
    path('articles/<slug:categID>', categoryShow)
]