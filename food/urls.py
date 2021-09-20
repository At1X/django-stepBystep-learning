from django.urls import path
from .views import homeView

app_name = 'foodUrl'

urlpatterns = [
    path('', homeView)
]