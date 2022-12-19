from django.db import models
from .items import Item

class Receipt(models.Model):
    id_user = models.IntegerField()
    name_cus = models.CharField(max_length=255)
    email_cus = models.EmailField()
    phone_cus = models.CharField(max_length=255)
    address_cus = models.TextField()
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    note = models.TextField()

    def __str__(self):
        return self.receipt_code