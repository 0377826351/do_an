# Generated by Django 4.0.4 on 2022-12-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degray', '0004_cart_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='status',
            field=models.BooleanField(),
        ),
    ]
