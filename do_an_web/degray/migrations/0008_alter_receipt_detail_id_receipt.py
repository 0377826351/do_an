# Generated by Django 4.0.4 on 2022-12-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degray', '0007_remove_receipt_detail_id_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt_detail',
            name='id_receipt',
            field=models.IntegerField(),
        ),
    ]