from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserForm, User, Product, Cart, WishListForm, WishList, CartForm

# Create your views here.
def home(request):
	return render(request, 'yinc/index.html', locals())

def signUp(request):
	form = UserForm()
	return render(request, 'yinc/signUp.html', locals())

def contactUs(request):
	return render(request, 'yinc/contactUs.html', locals())

def shoes(request):
	orderby = Product.objects.order_by('productId')
	return render(request, 'yinc/shoes.html', locals())

def jeans(request):
	orderby = Product.objects.order_by('productId')
	return render(request, 'yinc/jeans.html', locals())


def shirt(request):
	orderby = Product.objects.order_by('productId')
	return render(request, 'yinc/shirt.html', locals())

def addToCart(request):
	if request.method == 'POST':
		cartProductID = request.POST.get('productId')
		p=Cart(productId = cartProductID,)
		p.save();
	return HttpResponseRedirect("/yinc/home") 
	#form =CartForm();
	#return render(request, 'yinc/home.html', locals())

def addToWishList(request):
	if request.method == 'POST':
		cartProductID = request.POST.get('productId')
		p=WishList(productId = cartProductID,)
		p.save();
	return HttpResponseRedirect("/yinc/home")

def addUser(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		username = request.POST.get('username')
		phone = request.POST.get('phone')
		address = request.POST.get('address')
		pinCode = request.POST.get('pinCode')
		userId = "abc"
		p=User(userId = userId, userName = username, userPassword = password, email = email, phone = phone, address = address, pincode = pinCode, 
			)
		p.save();
	return HttpResponseRedirect("/yinc/home") 

