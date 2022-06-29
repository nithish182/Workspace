from django.urls import path
from home import views

#url's
urlpatterns = [
    path("",views.home,name='home'),
    path("products",views.products,name='products'),
    path("contact",views.contact,name='contact')
]