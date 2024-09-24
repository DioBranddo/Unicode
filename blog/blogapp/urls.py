from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), #Login Page
    path('register/', views.register, name='register'), #Register Page
    path('myblogs/', views.myblogs, name='myblogs'), #GET all blogs from a single user
    path('delete/', views.delete, name='delete'), #GET single blog from user and option to delete it
]