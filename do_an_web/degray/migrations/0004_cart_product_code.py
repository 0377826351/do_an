# Generated by Django 4.0.4 on 2022-12-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degray', '0003_cart_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_code',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
