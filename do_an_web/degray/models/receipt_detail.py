from django.db import models
from .items import Item
from .receipt import Receipt


class Receipt_DeTail(models.Model):
    id_receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE)
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name_item =models.CharField(max_length=255)
    item_size = models.CharField(max_length=255,null=True)
    qty_item = models.IntegerField()
    price = models.BigIntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.id_receipt