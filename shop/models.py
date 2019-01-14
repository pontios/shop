from django.conf import settings
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

User = settings.AUTH_USER_MODEL

class Category(MPTTModel):
    """Категории товаров"""
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children')
    slug = models.SlugField(max_length=100, unique=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара"""
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    price = models.IntegerField("Цена", default=0)
    slug = models.SlugField(max_length=150)
    availability = models.BooleanField("Наличие", default=True)
    quantity = models.IntegerField("Количество", default=1)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title

# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#
#     def sub_total(self):
#         return self.product.price * self.quantity
#
#
#     def __str__(self):
#         return self.product.title
#
#
# class Cart(models.Model):
#     """Корзина"""
#     item = models.ManyToManyField(CartItem,  blank=True)
#     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
#     date_added = models.DateField(auto_now_add=True)
#     total = models.IntegerField("Сумма", default=0)
#     accepted = models.BooleanField("Oбработано", default=True)
#
#     class Meta:
#         ordering = ['date_added']
#
#         def __str__(self):
#             return self.id

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.slug
