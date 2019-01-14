from django.urls import path
from django.conf.urls import  url

from . import views


urlpatterns = [
    path("", views.ProductsList.as_view(), name="product_all"),
    path('detail/<slug:slug>', views.ProductDetail.as_view(), name='product_detail'),
    path('cart/', views.CartDetail.as_view(), name="cart"),
    path('add/<int:product_id>', views.add_cart.as_view(), name='add_cart'),
]