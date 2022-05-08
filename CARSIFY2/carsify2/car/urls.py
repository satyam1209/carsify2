from django.contrib import admin
from django.urls import path
from car import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.user_login, name="login"),
    path('signup/', views.signup, name="signup"),
]