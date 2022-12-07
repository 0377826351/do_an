from django.db import models
from .category import Category
from django.conf import settings

class Item(models.Model):
    name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255)
    price = models.IntegerField()
    detai = models.TextField()
    image = models.ImageField(null=True)
    category_item = models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name