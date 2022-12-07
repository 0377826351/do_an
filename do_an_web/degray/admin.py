from django.contrib import admin
from .models import Receipt,Item,Customer,Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Customer)
admin.site.register(Receipt)