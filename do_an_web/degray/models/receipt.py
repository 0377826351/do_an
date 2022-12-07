from django.db import models
from .items import Item


class Receipt(models.Model):
    receipt_code = models.CharField(max_length=255)
    name_cus = models.CharField(max_length=255)
    email_cus = models.EmailField()
    phone_cus = models.CharField(max_length=255)
    address_cus = models.TextField()
    name_item = models.ForeignKey(Item,on_delete=models.CASCADE)
    qty_item = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    note = models.TextField()

    def __str__(self):
        return self.receipt_code