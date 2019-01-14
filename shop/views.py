# from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView

from .models import Product, Cart, CartItem
User = settings.AUTH_USER_MODEL
class ProductsList(ListView):
    """Список всех продуктов"""
    model = Product
    template_name = "shop/list-product.html"


class ProductDetail(DetailView):
    """Карточка товара"""
    model = Product
    context_object_name = 'product'
    template_name = 'shop/product-detail.html'


# def _cart_id(request):
#     cart = request.user.id
#     if not cart:
#         cart = Cart.objects.create(cart_id=cart)
#     return cart

class add_cart(View):

    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        try:
            cart = Cart.objects.get(cart_id=request.user.id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id=request.user.id
            )
            cart.save()
        try:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product=product,
                quantity=1,
                cart=cart
            )
            cart_item.save()
        return redirect('/cart/')

class CartDetail(View):

    def get(self, request):
        cart = Cart.objects.get(cart_id=request.user.id)
        cart_item = CartItem.objects.filter(cart=cart, active=True)
        context = {'cart_item': cart_item}
        return render(request, 'shop/cart.html', context)

# class CartDetail(View):
#
#     def get(self, request):
#         user = request.user.id
#         cart_user = Cart.objects.get(user_id=user)
#         cart_id = cart_user.id
#         cart = Cart.objects.get(id=cart_id)
#         context = {'cart': cart}
#         print(cart_id)
#         return render(request, 'shop/cart.html', context)
#
# class add_to_cart(View):
#
#     def get(self, request, product_id):
#         product = Product.objects.get(id=product_id)
#         new = CartItem.objects.get_or_create(product=product)
#         user = request.user.id
#         cart_user = Cart.objects.get(user_id=user)
#         cart_id = cart_user.id
#         cart = Cart.objects.get(id=cart_id)
#         if new not in cart.item.all():
#             cart.item.add(new)
#             cart.save()
#             return HttpResponseRedirect('/cart/')
