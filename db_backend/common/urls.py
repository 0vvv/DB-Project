from django.urls import path
from . import views


urlpatterns = [
    path('index', views.loginUser),
    path('register', views.registerUser),
    path('logout', views.logoutUser),
    path('user',views.getUser),
    path('search',views.searchPoem),
]