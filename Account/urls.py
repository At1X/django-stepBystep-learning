from django.contrib.auth import views
from .views import myOwnLogin , signup, activate
from django.urls import path, re_path
from .views import (
                        TheHome,
                        MyCreateView,
                        MyUpdateView,
                        AuthorDeleteView,
                        ProfileView,
)
app_name = 'account'

urlpatterns = [
    path('', TheHome.as_view(), name='home' ),
    path('create', MyCreateView.as_view(), name='createArticle'),
    path('update/<int:pk>', MyUpdateView.as_view(), name='updateArticle'),
    path('delete/<int:pk>', AuthorDeleteView.as_view(), name='deleteArticle'),
    path('profile', ProfileView.as_view(), name='userProfile'),
    path('signup', signup, name='signup'),
]