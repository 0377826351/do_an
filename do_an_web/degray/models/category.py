from django.db import models

class Category(models.Model):
    alias_category = models.CharField(max_length=255)
    name = models.CharField( max_length=255)
    active = models.BooleanField(null=True)

    def __str__(self):
        return self.name
