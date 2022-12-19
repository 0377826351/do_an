from django.contrib import admin
from .models import Receipt,Item,Category,Receipt_DeTail,Cart

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Receipt)
admin.site.register(Receipt_DeTail)
admin.site.register(Cart)