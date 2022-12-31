from django.db import models
from django.conf import settings

class Cart(models.Model):
    user_add = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)
    product_code = models.CharField(max_length=255,default=None)
    item_name = models.CharField(max_length=255)
    item_size = models.CharField(max_length=255,null=True)
    qty = models.IntegerField()
    price = models.IntegerField(default=0)
    image = models.ImageField(default=None)
    add_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.item_name