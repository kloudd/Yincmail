from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
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
    


    url(r'^api/product/$', views.ProductList.as_view()),
    url(r'^api/product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),

    url(r'^api/user/$', views.UserList.as_view()),
    url(r'^api/user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^api/cart/$', views.CartList.as_view()),
    url(r'^api/cart/(?P<pk>[0-9]+)/$', views.CartDetail.as_view()),

    url(r'^api/wishList/$', views.WishListList.as_view()),
    url(r'^api/wishList/(?P<pk>[0-9]+)/$', views.WishListDetail.as_view()),



]
urlpatterns = format_suffix_patterns(urlpatterns)