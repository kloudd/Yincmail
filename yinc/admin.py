from django.contrib import admin
from yinc.models import Product, User, WishList, Cart
# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(WishList)
admin.site.register(Cart)