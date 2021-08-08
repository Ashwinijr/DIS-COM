# Generated by Django 3.1.2 on 2020-10-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]