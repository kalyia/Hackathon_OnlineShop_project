
from django.db import models
from django.conf import settings

from apps.category.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='product/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name='product')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class LikeProduct(models.Model):
        user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
        product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name="likes")
        is_like = models.BooleanField(default=True)
<<<<<<< HEAD
=======

>>>>>>> d577f79bd345bea0c6f4dc89a83266c4f9c66bd5

