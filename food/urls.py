from django.urls import path
from .views import  DetDetailView, CategoryShow, base

app_name = 'foodUrl'

urlpatterns = [
    path('',base.as_view() , name='home'),
    path('<slug:theSLUG>',DetDetailView.as_view(), name='detailView'),
    path('articles/<slug:categID>', CategoryShow.as_view(), name='categClass')
]