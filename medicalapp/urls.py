from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('log/',views.log,name="log"),
    path('home/',views.home,name="home"),
    path('home1/',views.home1,name="home1"),
    path('home2/',views.home2,name="home2"),
]