# Generated by Django 5.1 on 2024-09-29 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_currency_product_format_product_old_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]