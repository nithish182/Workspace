from django.urls import path

#url's
urlpatterns = [
    path("register",views.register,name='register'),
    path("login",views.login,name='login'),
]