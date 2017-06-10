from django.db import models
from django .forms import ModelForm

# Create your models here.

class Product(models.Model):
	productId = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	imageUrl = models.CharField(max_length=200)
	price = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	weight = models.CharField(max_length=200)
	quantitiy = models.CharField(max_length=200)


class User(models.Model):
	userId = models.CharField(max_length=200, null=True)
	userName = models.CharField(max_length=200, null=True)
	userPassword = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	pincode = models.CharField(max_length=200, null=True)

class Cart(models.Model):
	productId = models.CharField(max_length=200)

class WishList(models.Model):
	productId = models.CharField(max_length=200)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'

class WishListForm(ModelForm):
    class Meta:
        model = WishList
        fields = '__all__'
