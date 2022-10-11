from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('register/', views.register_page, name="register"),

    path('users/<str:pk>/', views.user_details, name="user_details"),
    path('my-account/', views.my_account, name="my_account"),
    path('my-account/edit', views.update_account, name="update_account"),
    path('my-account/change-password', views.change_password, name="change_password"),

]