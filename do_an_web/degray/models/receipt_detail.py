from django.db import models
from .items import Item
from .receipt import Receipt


class Receipt_DeTail(models.Model):
    id_receipt = models.IntegerField()
    name_item =models.CharField(max_length=255)
    item_size = models.CharField(max_length=255,null=True)
    qty_item = models.IntegerField()
    price = models.BigIntegerField()
    image = models.ImageField()

    def __int__(self):
        return self.id_receipt