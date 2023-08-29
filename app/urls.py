from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("register",views.register,name="register"),
    path("loginpage",views.loginpage,name="loginpage"),
    path('login',views.login,name='login'),
    path("update",views.update,name="update"),
    path("delete",views.delete,name="delete"),
    path("update",views.update,name="update"),
]