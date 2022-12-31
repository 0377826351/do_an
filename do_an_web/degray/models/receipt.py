from django.db import models
from .items import Item

STATUS_CHOICES =(
    ("1","Đã Khởi Tạo"),
    ("2","Đang Giao Hàng"),
    ("3","Giao Thành Công"),
    ("4","Bị Hủy"),
)

class Receipt(models.Model):
    id_user = models.IntegerField()
    name_cus = models.CharField(max_length=255)
    email_cus = models.EmailField()
    phone_cus = models.CharField(max_length=255)
    address_cus = models.TextField()
    status = models.CharField(max_length=255,choices=STATUS_CHOICES,default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    note = models.TextField(null=True)

    def __str__(self):
        return self.name_cus