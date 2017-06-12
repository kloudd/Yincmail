from rest_framework import serializers
from .models import UserForm, User, Product, Cart, WishListForm, WishList, CartForm


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('productId', 'name', 'imageUrl', 'price', 'category', 'weight', 'quantitiy')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'userName', 'userPassword', 'email', 'phone', 'address', 'pincode')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = '__all__'