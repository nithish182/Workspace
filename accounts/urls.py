from django.urls import path
from accounts import views

#url's
urlpatterns = [
    path("register",views.register,name='register'),
    path("login",views.login,name='login'),
]