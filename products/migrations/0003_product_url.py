# Generated by Django 3.1.2 on 2020-10-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]