from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('login/', views.login_page, name="login"),

    path('users/<str:pk>/', views.user_details, name="user_details"),
    path('my-account/', views.my_account, name="my_account"),

]