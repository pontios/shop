from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Product, Cart, CartItem

class CategoryMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

admin.site.register(Category, CategoryMPTTModelAdmin)
admin.site.register(Product)
admin.site.register(Cart)
#admin.site.register(CartItem)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'active']
    list_filter = ['active']
    list_editable = ['active']
admin.site.register(CartItem, CartItemAdmin)




