# Generated by Django 4.0.4 on 2022-12-25 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degray', '0010_extend_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='note',
            field=models.TextField(null=True),
        ),
    ]
