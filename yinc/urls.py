from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^signUp/$', views.signUp, name='signUp'),
    url(r'^contactUs/$', views.contactUs, name='contactUs'),
    url(r'^home/shoes/$', views.shoes, name='shoes'),
    url(r'^home/shirt/$', views.shirt, name='shirt'),
    url(r'^home/jeans/$', views.jeans, name='jeans'),

    url(r'^controller/addToCart/$', views.addToCart, name='addToCart'),
    url(r'^controller/addToWishList/$', views.addToWishList, name='addToWishList'),
    url(r'^controller/addUser/$', views.addUser, name='addUser'),
]